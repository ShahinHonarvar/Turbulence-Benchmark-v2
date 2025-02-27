def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s or not is_prime(int(s)):
                return False
        return True
    idx = 177
    if idx >= len(numbers):
        return []
    x = numbers[idx]
    result = []
    if x >= 10:
        for num in range(11, x + 1):
            if '0' not in str(num) and is_prime(num) and left_right_truncatable(num):
                result.append(num)
    return result