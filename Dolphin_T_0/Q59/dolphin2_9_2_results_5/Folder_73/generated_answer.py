def all_left_truncatable_prime(x):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_truncatable(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[i:])):
                return False
        return True
    primes = [i for i in range(x) if is_prime(i) and is_truncatable(i)]
    return sorted(primes)