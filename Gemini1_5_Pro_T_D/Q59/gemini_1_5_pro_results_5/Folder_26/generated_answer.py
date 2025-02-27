def all_left_truncatable_prime(numbers):
    x = numbers[81]

    def is_left_truncatable_prime(n):
        if n < 10 and n > 0:
            return n > 1
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            if int(s[i:]) % 2 == 0:
                return False
            if not is_prime(int(s[i:])):
                return False
        return is_prime(n)

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            result.append(i)
    result.sort(reverse=True)
    return result