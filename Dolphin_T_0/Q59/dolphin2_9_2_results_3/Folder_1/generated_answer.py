def all_left_truncatable_prime(primes):
    numbers = []
    for prime in primes:
        if not '0' in str(prime):
            if all((is_prime(int(str(prime)[i:])) for i in range(1, len(str(prime))))):
                numbers.append(prime)
    return sorted(numbers, reverse=True)