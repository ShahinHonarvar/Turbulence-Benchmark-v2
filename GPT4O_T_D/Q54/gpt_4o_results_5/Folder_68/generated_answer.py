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

    def generate_right_truncatable_primes(n):
        result = []
        candidates = [2, 3, 5, 7]
        while candidates:
            candidate = candidates.pop()
            if candidate < n:
                result.append(candidate)
                for last_digit in [1, 3, 7, 9]:
                    new_candidate = candidate * 10 + last_digit
                    if is_prime(new_candidate):
                        candidates.append(new_candidate)
        return result
    x = numbers[1]
    right_truncatable_primes = generate_right_truncatable_primes(x)
    return sorted(right_truncatable_primes, reverse=True)