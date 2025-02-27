def all_left_right_truncatable_prime(args):
    x = args[97]
    primes = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for num in range(x, 1, -1):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                while len(str_num) > 1:
                    if not is_prime(int(str_num[1:-1])):
                        break
                    str_num = str_num[1:-1]
                if len(str_num) == 1 and is_prime(int(str_num)):
                    primes.append(num)
    return primes[::-1]