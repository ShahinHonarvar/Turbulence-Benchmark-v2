def all_right_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[126]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncated = num
            while truncated > 0:
                truncated //= 10
                if truncated > 0 and (not is_prime(truncated)):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)