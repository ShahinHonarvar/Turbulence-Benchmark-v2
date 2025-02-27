def all_left_right_truncatable_prime(numbers):
    x = numbers[6]
    truncatable_primes = []

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
        for i in range(len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    for num in range(x, 1, -1):
        if is_truncatable_prime(num):
            truncatable_primes.append(num)
    return truncatable_primes