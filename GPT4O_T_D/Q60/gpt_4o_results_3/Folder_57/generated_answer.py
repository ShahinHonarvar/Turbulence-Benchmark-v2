def all_left_right_truncatable_prime(numbers):
    x = numbers[54]

    def is_prime(n):
        if n <= 1:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        str_n = str(n)
        for i in range(len(str_n)):
            left_trunc = int(str_n[i:])
            right_trunc = int(str_n[:len(str_n) - i])
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    result = [n for n in range(2, x + 1) if is_prime(n) and is_truncatable_prime(n)]
    return sorted(result, reverse=True)