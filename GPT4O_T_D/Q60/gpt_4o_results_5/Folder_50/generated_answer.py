def all_left_right_truncatable_prime(numbers):
    x = numbers[57]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n)):
            left_trunc = int(str_n[i:]) if str_n[i:] else 0
            right_trunc = int(str_n[:i + 1]) if str_n[:i + 1] else 0
            if not is_prime(left_trunc) or not is_prime(right_trunc):
                return False
        return True
    result = [i for i in range(2, x + 1) if is_prime(i) and is_truncatable_prime(i)]
    return sorted(result, reverse=True)