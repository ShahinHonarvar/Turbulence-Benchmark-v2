import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num_tuple):
    x = num_tuple[55]
    left_truncatable_prime_list = []
    for num in range(x, 1, -1):
        if is_prime(num):
            trunc_num = num
            while trunc_num > 1:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                left_truncatable_prime_list.append(num)
    return sorted(left_truncatable_prime_list, reverse=True)