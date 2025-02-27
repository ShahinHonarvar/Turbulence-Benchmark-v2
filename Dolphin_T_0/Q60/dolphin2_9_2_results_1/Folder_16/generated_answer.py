def is_prime(num):
    if num in (0, 1):
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(pos_int_tuple):
    x = pos_int_tuple[792]
    left_right_truncatable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num):
            str_num = str(num)
            while len(str_num) > 1:
                if str_num.pop(0) == '0' or str_num.pop(-1) == '0':
                    break
            if is_prime(int(str_num)):
                left_right_truncatable_primes.append(num)
    return sorted(left_right_truncatable_primes)