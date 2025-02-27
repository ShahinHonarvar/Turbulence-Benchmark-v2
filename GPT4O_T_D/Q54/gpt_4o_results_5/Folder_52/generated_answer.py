def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_right_truncatable_primes(limit):
        right_truncatable_primes = [2, 3, 5, 7]
        new_primes = right_truncatable_primes[:]
        while new_primes:
            current = new_primes.pop(0)
            for digit in range(10):
                candidate = current * 10 + digit
                if candidate < limit and is_prime(candidate):
                    right_truncatable_primes.append(candidate)
                    new_primes.append(candidate)
        return right_truncatable_primes
    if len(numbers) <= 52:
        return []
    x = numbers[52]
    if x <= 0:
        return []
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes, reverse=True)