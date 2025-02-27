def all_left_truncatable_prime(integers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    x = integers[73]
    left_truncatable_primes = [n for n in range(2, x) if is_left_truncatable_prime(n)]
    return sorted(left_truncatable_primes, reverse=True)