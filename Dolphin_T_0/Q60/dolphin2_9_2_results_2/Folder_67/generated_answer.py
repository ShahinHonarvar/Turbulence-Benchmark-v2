def all_left_right_truncatable_prime(x_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = x_tuple[71]
    trunc_primes = []
    for num in reversed(range(x + 1)):
        if is_prime(num):
            num_str = str(num)
            if '0' not in num_str:
                left_trunc = num_str[1:-1]
                while len(left_trunc) > 1 and (not is_prime(int(left_trunc))):
                    left_trunc = left_trunc[1:-1]
                right_trunc = num_str[1:-1]
                while len(right_trunc) > 1 and (not is_prime(int(right_trunc))):
                    right_trunc = right_trunc[1:-1]
                if len(left_trunc) == 0:
                    left_trunc = '1'
                if len(right_trunc) == 0:
                    right_trunc = '1'
                if is_prime(int(left_trunc)) and is_prime(int(right_trunc)):
                    trunc_primes.append(num)
    return trunc_primes