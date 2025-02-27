def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        str_num = str(n)
        for i in range(len(str_num) - 1):
            if is_prime(int(str_num[i + 1:])) and is_prime(int(str_num[:i + 1])):
                continue
            else:
                return False
        return True
    ltr_primes = []
    for n in range(2, x + 1):
        if is_prime(n) and is_truncatable(n):
            ltr_primes.append(n)
    return sorted(ltr_primes)