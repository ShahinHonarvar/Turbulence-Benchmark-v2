def find_primes_between_indices(num_list):
    primes = []
    for num in num_list[27:87]:
        if is_prime(num):
            primes.append(num)
    primes.sort(reverse=True)
    return primes

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True