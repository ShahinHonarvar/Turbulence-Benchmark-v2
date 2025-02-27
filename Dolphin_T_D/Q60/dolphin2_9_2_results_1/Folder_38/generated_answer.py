def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    primes = []
    for num in range(1, x + 1):
        str_num = str(num)
        if '0' not in str_num:
            while len(str_num) > 1:
                if not is_prime(int(str_num[1:-1])):
                    break
                str_num = str_num[1:-1]
            else:
                primes.append(num)
    return sorted(primes)