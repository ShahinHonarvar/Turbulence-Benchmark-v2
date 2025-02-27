def all_right_truncatable_prime(a_tuple):
    x = a_tuple[71]
    right_truncatable_prime_list = []
    for num in range(2, x):
        if is_prime(num):
            trunc_num = num
            while trunc_num != 0:
                if not is_prime(trunc_num):
                    break
                trunc_num //= 10
            else:
                right_truncatable_prime_list.append(num)
    return sorted(right_truncatable_prime_list, reverse=True)

def is_prime(n):
    if n == 1 or n == 0:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True