def all_left_right_truncatable_prime(numbers):
    if len(numbers) <= 803:
        return []
    x = numbers[803]

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
        str_n = str(n)
        length = len(str_n)
        for i in range(1, length):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:-i])
            if not (is_prime(left_trunc) and is_prime(right_trunc)):
                return False
        return is_prime(n)
    result = []
    for num in range(10, x + 1):
        if is_truncatable_prime(num):
            result.append(num)
    return result