def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(1, len(num_list) + 1):
        if is_prime(i):
            prime_list.append(i)
    return sorted(prime_list, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True