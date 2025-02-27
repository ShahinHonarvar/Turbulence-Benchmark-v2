def all_right_truncatable_prime(n):
    x = n[792]

    def is_prime(num):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable_prime(num):
        num_str = str(num)
        for i in range(1, len(num_str)):
            if not is_prime(int(num_str[:-i])):
                return False
        return True
    result = []
    for num in range(2, x):
        if is_prime(num) and is_truncatable_prime(num):
            result.append(num)
    result.sort()
    return result