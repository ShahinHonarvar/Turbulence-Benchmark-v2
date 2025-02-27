def all_left_right_truncatable_prime(tup):
    x = tup[7]
    truncatable_primes = []
    for num in range(x, 1, -1):
        if num < 10:
            continue
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                if left_right_trun(str_num, len(str_num)):
                    truncatable_primes.append(num)
    return truncatable_primes

def left_right_trun(n, len_n):
    if len_n == 2:
        return is_prime(int(n[1])) and is_prime(int(n[0]))
    else:
        return is_prime(int(n[1:len_n])) and is_prime(int(n[0:len_n - 1])) and left_right_trun(n[0:len_n - 1], len_n - 1)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True