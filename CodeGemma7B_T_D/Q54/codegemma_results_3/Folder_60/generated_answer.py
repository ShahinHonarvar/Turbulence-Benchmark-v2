def all_right_truncatable_prime(tupled_int):
    x = tupled_int[87]
    right_truncatable_primes = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncatable(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            trunc_num = int(str_num[:-i])
            if not is_prime(trunc_num):
                return False
        return True
    for i in range(2, x):
        if is_prime(i) and right_truncatable(i):
            right_truncatable_primes.append(i)
    right_truncatable_primes.sort()
    return right_truncatable_primes