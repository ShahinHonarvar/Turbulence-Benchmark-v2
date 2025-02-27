def all_left_truncatable_prime(n_tuple):

    def is_prime(n):
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        sqrt_n = int(n ** 0.5) + 1
        for i in range(3, sqrt_n, 2):
            if n % i == 0:
                return False
        return True
    x = n_tuple[8]
    all_left_trunc_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            str_num = str(num)
            for i in range(len(str_num) - 1):
                if not is_prime(int(str_num[i + 1:])):
                    break
                if i == len(str_num) - 2:
                    all_left_trunc_primes.append(num)
    return all_left_trunc_primes