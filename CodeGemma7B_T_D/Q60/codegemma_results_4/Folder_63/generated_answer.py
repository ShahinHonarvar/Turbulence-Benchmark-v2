from sympy import isprime

def all_left_right_truncatable_prime(x):
    x = int(x[88])
    result = []
    for i in range(2, x):
        if '0' not in str(i):
            j = 2 * i
            if isprime(i):
                right_flag = True
                left_flag = True
                while j < x and (right_flag or left_flag):
                    if not isprime(j):
                        right_flag = False
                    if not isprime(int(str(i)[:j % 10])):
                        left_flag = False
                    j += i
                if right_flag and left_flag:
                    result.append(i)
    return sorted(result)