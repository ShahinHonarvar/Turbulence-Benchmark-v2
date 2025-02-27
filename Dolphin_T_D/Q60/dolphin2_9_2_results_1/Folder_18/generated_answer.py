def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(lst):
    x = lst[429]
    primes = []
    for num in range(x, 0, -1):
        str_num = str(num)
        if '0' not in str_num and is_prime(num):
            trunc = len(str_num) >= 3 and is_prime(int(str_num[1:-1]))
            while trunc and len(str_num) > 2:
                trunc = trunc and is_prime(int(str_num[1:-1]))
                str_num = str_num[1:-1]
                if not trunc:
                    break
            if trunc:
                primes.append(num)
    return sorted(primes, reverse=True)