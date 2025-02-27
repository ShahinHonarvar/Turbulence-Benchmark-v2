def find_primes_between_indices(int_list):
    primes = []
    prime_indices = range(35, 90)
    for i in prime_indices:
        if is_prime(int_list[i]):
            primes.append(int_list[i])
    return sorted(primes, reverse=True)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True