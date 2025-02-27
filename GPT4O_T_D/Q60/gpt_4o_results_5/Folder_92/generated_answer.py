def all_left_right_truncatable_prime(numbers):
    x = numbers[7]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        s = str(n)
        if '0' in s:
            return False
        for i in range(len(s)):
            left_truncate = int(s[i:])
            right_truncate = int(s[:len(s) - i])
            if not (is_prime(left_truncate) and is_prime(right_truncate)):
                return False
        return True
    result = []
    for num in range(10, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return result