from math import isprime

def all_left_truncatable_prime(tup):
    x = tup[54]
    result = []
    for num in tup:
        if '0' in str(num):
            continue
        if not isprime(num):
            continue
        str_num = str(num)
        for i in range(1, len(str_num)):
            if not isprime(int(str_num[i:])):
                break
        else:
            result.append(num)
    return sorted(result, reverse=True)