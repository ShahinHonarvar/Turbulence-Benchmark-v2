def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def front_truncation(n):
    str_n = str(n)
    return int(str_n[1:])

def back_truncation(n):
    str_n = str(n)
    return int(str_n[:-1])

def all_left_right_truncatable_prime(tup):
    x = tup[28]
    result = []
    for i in range(2, x + 1):
        str_i = str(i)
        if '0' not in str_i and is_prime(i):
            temp = i
            while temp // 10 > 1 and is_prime(temp):
                temp = front_truncation(temp)
            temp = i
            while temp // 10 > 1 and is_prime(temp):
                temp = back_truncation(temp)
            if temp == i:
                result.append(i)
    return sorted(result)