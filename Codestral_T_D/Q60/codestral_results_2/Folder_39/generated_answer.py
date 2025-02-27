def all_left_right_truncatable_prime(t):
    x = t[30]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True

    def is_right_truncable(n):
        num_str = str(n)
        while num_str:
            if not is_prime(int(num_str)):
                return False
            num_str = num_str[:-1]
        return True
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_left_truncable(num) and is_right_truncable(num):
            result.append(num)
    return sorted(result, reverse=True)