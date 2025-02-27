def all_right_truncatable_prime(tupl):
    x = tupl[20]
    rtps = []

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncatable_primes(num):
        str_num = str(num)
        for i in range(len(str_num) - 2, -1, -1):
            str_num = str_num[:i] + str_num[i + 1:]
            num = int(str_num)
            if is_prime(num):
                if num not in rtps:
                    rtps.append(num)
    for num in tupl:
        if num <= x:
            right_truncatable_primes(num)
    rtps.sort(reverse=True)
    return rtps