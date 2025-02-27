import math

def all_right_truncatable_prime(lst):
    x = lst[975]
    prime_list = []
    for num in range(2, x):
        if is_prime(num):
            trunc_num = num
            while len(str(trunc_num)) > 0:
                if not is_prime(trunc_num):
                    break
                trunc_num = trunc_num // 10
            else:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True