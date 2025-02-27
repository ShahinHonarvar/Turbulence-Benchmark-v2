def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if not s:
                return True
            if '0' in s or not is_prime(int(s)):
                return False
        return True

    def left_right_truncatable(n):
        return is_prime(n) and is_truncatable(n)
    x = numbers[67]
    result = [i for i in range(10, x + 1) if left_right_truncatable(i)]
    return sorted(result, reverse=True)