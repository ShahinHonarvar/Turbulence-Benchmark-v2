def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        s = str(n)
        while len(s) > 0:
            if not is_prime(int(s)):
                return False
            s = s[1:] if len(s) == 1 else s[1:-1]
        return True
    x = numbers[14]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_truncatable_prime(num):
            result.append(num)
    return sorted(result)