def all_left_truncatable_prime(numbers):
    x = numbers[69]

    def is_left_truncatable_prime(num):
        if num < 10 and num > 1:
            return True
        if '0' in str(num) or num < 10:
            return False
        s = str(num)
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0:
                return False
            if not is_prime(int(s[i:])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            res.append(i)
    res.sort(reverse=True)
    return res