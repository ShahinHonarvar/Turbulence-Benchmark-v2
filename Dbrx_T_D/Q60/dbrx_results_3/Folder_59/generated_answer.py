from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[84]
    result = []
    for num in range(2, x + 1):
        if isprime(num):
            num_str = str(num)
            flag = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])) or not isprime(int(num_str[:i])):
                    flag = False
                    break
            if flag:
                result.append(num)
    result.sort(reverse=True)
    return result