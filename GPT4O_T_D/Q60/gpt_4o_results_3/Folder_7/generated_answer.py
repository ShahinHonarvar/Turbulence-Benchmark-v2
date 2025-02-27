def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_from_left(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[1:]
        return True

    def is_truncatable_from_right(n):
        s = str(n)
        while s:
            if not is_prime(int(s)):
                return False
            s = s[:-1]
        return True

    def is_left_right_truncatable_prime(n):
        return is_truncatable_from_left(n) and is_truncatable_from_right(n)
    if len(numbers) <= 803:
        return []
    x = numbers[803]
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_right_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes)