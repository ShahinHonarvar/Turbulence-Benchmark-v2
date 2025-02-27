def all_left_right_truncatable_prime(x):

    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

    def is_truncatable(x):
        s = str(x)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            left = int(s[i:])
            right = int(s[:len(s) - i])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = []
    for num in range(x + 1):
        if is_truncatable(num):
            result.append(num)
    result.sort(reverse=True)
    return result