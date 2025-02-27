def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[8]
    lst = []
    for num in range(2, x + 1):
        if is_prime(num):
            str_num = str(num)
            if '0' not in str_num:
                if all((is_prime(int(str_num[i:])) and is_prime(int(str_num[:-i])) for i in range(1, len(str_num)))):
                    lst.append(num)
    return sorted(lst, reverse=True)