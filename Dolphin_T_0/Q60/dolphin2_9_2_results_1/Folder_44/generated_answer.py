def all_left_right_truncatable_prime(num_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = num_tuple[39]
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if not all((int(d) != 0 for d in str_num)):
            continue
        if not is_prime(num):
            continue
        for _ in range(len(str_num) - 1):
            str_num = str_num[1:-1]
            if not str_num:
                left_right_truncatable_primes.append(num)
                break
            if not is_prime(int(str_num)):
                break
    return sorted(left_right_truncatable_primes)