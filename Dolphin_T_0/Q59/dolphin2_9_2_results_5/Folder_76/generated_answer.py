def all_left_truncatable_prime(numbers_sequence):
    x = numbers_sequence[370]
    left_truncatable_primes = []

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    for num in range(x, 1, -1):
        if is_prime(num) and '0' not in list(str(num)):
            truncated = num
            while truncated > 1:
                if not is_prime(truncated):
                    break
                truncated //= 10
            else:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)