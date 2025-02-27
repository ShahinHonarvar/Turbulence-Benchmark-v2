def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if str_n[i:] == '0' * len(str_n[i:]) or not is_prime(int(str_n[i:])):
                return False
            if str_n[:-i] == '0' * len(str_n[:-i]) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = numbers[29]
    return sorted([i for i in range(2, x + 1) if '0' not in str(i) and is_truncatable_prime(i)])