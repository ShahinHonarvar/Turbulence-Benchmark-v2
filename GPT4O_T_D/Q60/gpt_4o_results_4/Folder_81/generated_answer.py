def all_left_right_truncatable_prime(numbers):
    x = numbers[98]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        s = str(n)
        while len(s) > 1:
            s = s[1:-1]
            if s and (not is_prime(int(s))):
                return False
        return True
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    return result