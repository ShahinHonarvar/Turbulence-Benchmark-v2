def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(25, 73):
        if is_prime(num_list[i]):
            prime_list.append(num_list[i])
    prime_list.sort()
    return prime_list

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True