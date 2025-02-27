def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[784]
    left_truncatable_prime_list = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        str_n = str(n)
        if '0' in str_n:
            return False
        for i in range(len(str_n) - 1):
            if not is_prime(int(str_n[i:])):
                return False
        return True
    for i in range(x):
        if is_prime(i) and is_left_truncatable(i):
            left_truncatable_prime_list.append(i)
    return sorted(left_truncatable_prime_list)