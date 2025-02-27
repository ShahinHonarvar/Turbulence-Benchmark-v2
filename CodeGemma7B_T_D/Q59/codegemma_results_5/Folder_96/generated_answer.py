def all_left_truncatable_prime(tup):
    x = tup[29]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(num):
        if '0' in str(num):
            return False
        current_num = num
        while current_num != 0:
            if not is_prime(current_num):
                return False
            current_num //= 10
        return True
    result = []
    for num in range(2, x):
        if left_truncatable(num):
            result.append(num)
    return sorted(result)