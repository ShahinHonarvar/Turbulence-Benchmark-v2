def all_left_right_truncatable_prime(a_tuple):
    x = a_tuple[760]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_right_truncatable_primes = []
    for num in range(2, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            while len(str_num) > 1:
                if not is_prime(int(str_num)):
                    break
                if len(str_num) > 2:
                    if not is_prime(int(str_num[1:])) or not is_prime(int(str_num[:-1])):
                        break
                str_num = str_num[1:-1]
                if len(str_num) == 1 and is_prime(int(str_num)):
                    left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes, reverse=True) if left_right_truncatable_primes else []