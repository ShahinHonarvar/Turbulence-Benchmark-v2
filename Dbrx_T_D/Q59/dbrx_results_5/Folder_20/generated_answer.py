from sympy import isprime

def all_left_truncatable_prime(n):
    result = []
    for num in range(1, n):
        string_num = str(num)
        if '0' in string_num:
            continue
        flag = True
        for i in range(1, len(string_num)):
            if not isprime(int(string_num[i:])):
                flag = False
                break
        if flag:
            result.append(num)
    return sorted(result, reverse=True)