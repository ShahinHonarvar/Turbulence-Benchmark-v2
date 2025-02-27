def all_left_truncatable_prime(tup):
    res = []
    for num in tup:
        str_num = str(num)
        if '0' not in str_num and math.sqrt(num) > num // 2:
            if all_lefts(str_num):
                res.append(num)
    res.sort()
    return res

def all_lefts(str_num):
    l = len(str_num)
    for i in range(1, l):
        num = int(str_num[i:])
        if num == 2:
            continue
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0):
            return False
        for j in range(11, int(math.sqrt(num)) + 2, 2):
            if num % j == 0:
                return False
    return True