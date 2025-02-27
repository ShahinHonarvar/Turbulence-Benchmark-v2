def all_left_right_truncatable_prime(numbers):

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

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        for i in range(len(s)):
            left_truncated = int(s[i:])
            right_truncated = int(s[:len(s) - i])
            if not is_prime(left_truncated) or not is_prime(right_truncated):
                return False
        return True
    x = numbers[19]
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result