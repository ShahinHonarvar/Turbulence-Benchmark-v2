def all_left_right_truncatable_prime(args):
    x = args[70]

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    truncatable_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        str_num = str(num)
        i = 0
        while len(str_num) > 1:
            if is_prime(int(str_num)):
                str_num = str_num[1:-1]
            else:
                i = 1
                break
        if i == 0:
            truncatable_primes.append(num)
    return sorted(truncatable_primes)