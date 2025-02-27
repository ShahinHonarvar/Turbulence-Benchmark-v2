def find_primes_between_indices(numbers):
    primes = []
    for num in numbers[14:74]:
        if is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True) or []