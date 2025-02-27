def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        if '0' in s:
            return False
        while len(s) > 1:
            s = s[1:] if len(s) > 2 else s[:-1]
            if not is_prime(int(s)):
                return False
        return True
    if len(numbers) <= 69:
        return []
    x = numbers[69]
    truncatable_primes = []
    for number in range(11, x + 1):
        if is_prime(number) and is_truncatable_prime(number):
            truncatable_primes.append(number)
    return sorted(truncatable_primes, reverse=True)