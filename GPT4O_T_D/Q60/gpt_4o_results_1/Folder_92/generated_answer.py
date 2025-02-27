def all_left_right_truncatable_prime(numbers):
    x = numbers[7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:-i])):
                return False
        return True
    truncatable_primes = []
    for num in range(10, x + 1):
        if '0' not in str(num) and is_prime(num) and is_truncatable(num):
            truncatable_primes.append(num)
    return truncatable_primes