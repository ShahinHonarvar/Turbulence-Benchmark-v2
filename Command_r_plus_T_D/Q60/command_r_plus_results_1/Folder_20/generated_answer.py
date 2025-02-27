def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable_prime(num):
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not is_prime(int(str_num[:i])) or not is_prime(int(str_num[i:])) or str_num[0] == '0' or (str_num[-1] == '0'):
                return False
        return True
    primes = [i for i in range(2, x + 1) if is_prime(i)]
    truncatable_primes = [i for i in primes if is_left_right_truncatable_prime(i)]
    return sorted(truncatable_primes, reverse=True)