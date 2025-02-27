from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    result = []
    for num in range(1, x + 1):
        if isprime(num) and (not '0' in str(num)):
            flag = True
            num_str = str(num)
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                    flag = False
                    break
            if flag:
                result.append(num)
    return sorted(result, reverse=True)