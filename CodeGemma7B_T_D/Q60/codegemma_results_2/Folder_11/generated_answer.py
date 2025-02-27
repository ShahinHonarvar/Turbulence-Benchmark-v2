def all_left_right_truncatable_prime(t):
    x = t[86]
    i = 2
    result = []
    while i * i <= x:
        str_i = str(i)
        temp = i
        if '0' not in str_i and is_prime(temp):
            while temp // 10 != 0 and temp % 10 != 0 and is_prime(temp):
                temp //= 10
            if temp == 2 or temp == 3 or temp == 5 or (temp == 7):
                result.append(i)
        i += 1
    return sorted(result)

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True