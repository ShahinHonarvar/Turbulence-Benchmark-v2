def find_primes_between_indices(num_list):
    primes = []
    for i in range(len(num_list)):
        if is_prime(num_list[i]):
            primes.append(num_list[i])
    primes.sort()
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True