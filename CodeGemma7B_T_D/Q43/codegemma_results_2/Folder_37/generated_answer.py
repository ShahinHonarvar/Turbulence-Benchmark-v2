def find_primes_between_indices(number_list):
    prime_numbers = []
    for number in number_list[13:69]:
        if is_prime(number):
            prime_numbers.append(number)
    prime_numbers.sort()
    return prime_numbers

def is_prime(number):
    if number <= 1:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True