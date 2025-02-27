def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_between_indices(numbers_list):
    primes = []
    for num in numbers_list[458:782]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes)