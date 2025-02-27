def is_prime(n):
    if n in fac and n not in zero:
        return True
    else:
        return False

def check_prime_list(List):
    res = [x for x in List if is_prime(x)]
    return res

def right_trunc(n):
    temp = n
    list_num = []
    while temp > 0:
        list_num.append(temp % 10)
        temp //= 10
    list_num = list_num[::-1]
    return list_num

def is_trunc(n, List):
    list_num = right_trunc(n)
    for i in range(len(list_num)):
        remove_digit = list_num[i]
        temp_list = list_num.copy()
        temp_list.remove(remove_digit)
        if temp_list not in List:
            return False
    return True

def left_trunc(n):
    temp = n
    list_num = []
    while temp > 0:
        list_num.append(temp % 10)
        temp //= 10
    list_num.reverse()
    return list_num

def all_left_truncatable_prime(tup):
    prime_list = check_prime_list(zero)
    left_trunc_prime_list = []
    for i in range(1000):
        if is_trunc(tup[i], prime_list):
            left_trunc_prime_list.append(tup[i])
    left_trunc_prime_list.sort(reverse=True)
    return left_trunc_prime_list