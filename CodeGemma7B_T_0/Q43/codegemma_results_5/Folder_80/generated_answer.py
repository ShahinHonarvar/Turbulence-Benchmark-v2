def find_primes_between_indices(num_list):
    prime_list = []
    for i in range(13, 30):
        if is_prime(num_list[i]):
            prime_list.append(num_list[i])
    return sorted(prime_list, reverse=True)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True