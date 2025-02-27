def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[645]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            str_num = str(num)
            while str_num:
                if is_prime(int(str_num)):
                    str_num = str_num[1:]
                else:
                    break
            else:
                primes.append(num)
    return sorted(primes)