def all_left_right_truncatable_prime(numbers):
    x = numbers[35]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        s = str(num)
        while len(s) > 1:
            s = s[1:-1]
            if not s:
                break
            if '0' in s or not is_prime(int(s)):
                return False
        return True
    truncatable_primes = []
    for num in range(10, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)