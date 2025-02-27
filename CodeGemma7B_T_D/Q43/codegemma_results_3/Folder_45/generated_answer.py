def find_primes_between_indices(list_of_numbers):
    prime_list = []
    for number in list_of_numbers[23:40]:
        if is_prime(number):
            prime_list.append(number)
    return sorted(prime_list)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True