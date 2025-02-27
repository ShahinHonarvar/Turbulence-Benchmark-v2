def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2 or n % 2 == 0:
            return n == 2
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    x = numbers[43]
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    results = []
    for prime in primes:
        if all((is_prime((int(str(prime)[i:j]) for i in range(len(str(prime))))) for j in range(1, len(str(prime)) + 1))):
            results.append(prime)
    return sorted(results)