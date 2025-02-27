def all_left_right_truncatable_prime(num_tuple):
    num = num_tuple[54]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(1, len(str_n)):
            left = int(str_n[:i])
            right = int(str_n[i:])
            if not is_prime(left) or not is_prime(right):
                return False
        return True
    result = []
    for n in range(2, num + 1):
        if is_prime(n) and is_truncatable(n):
            result.append(n)
    return result