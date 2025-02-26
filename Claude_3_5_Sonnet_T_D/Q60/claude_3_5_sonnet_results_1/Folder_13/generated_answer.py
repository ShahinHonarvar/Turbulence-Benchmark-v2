def all_left_right_truncatable_prime(tuple_input):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_right_truncatable(n):
        if n < 10:
            return is_prime(n)
        s = str(n)
        if '0' in s:
            return False
        for i in range(1, len(s)):
            left = int(s[i:])
            right = int(s[:-i])
            if not (is_prime(left) and is_prime(right)):
                return False
        return is_prime(n)
    x = tuple_input[784]
    result = []
    for num in range(2, x + 1):
        if is_left_right_truncatable(num):
            result.append(num)
    return result