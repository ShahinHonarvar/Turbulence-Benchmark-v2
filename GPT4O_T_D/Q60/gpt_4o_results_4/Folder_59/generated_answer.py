def all_left_right_truncatable_prime(numbers):
    if len(numbers) < 85:
        return []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return True
    x = numbers[84]
    if x < 10:
        return []
    primes = []
    for num in range(10, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num) and is_left_right_truncatable(num):
            primes.append(num)
    return sorted(primes, reverse=True)