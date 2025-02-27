def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:]) if str(n)[1:] else 0
    x = t[1]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            truncated_num = num
            while truncated_num > 0:
                truncated_num = truncate_left(truncated_num)
                if not is_prime(truncated_num):
                    break
            else:
                result.append(num)
    return sorted(result, reverse=True)