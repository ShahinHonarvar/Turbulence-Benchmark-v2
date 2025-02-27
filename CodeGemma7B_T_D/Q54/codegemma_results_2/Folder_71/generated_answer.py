from sympy import *

def all_right_truncatable_prime(tupple_list):
    x = tupple_list[22]
    right_truncatable_prime_list = []
    for i in range(2, x):
        n = str(i)
        flag = True
        for j in range(len(n) - 1):
            n = n[:-1]
            if int(n) % prime(int(n)) != 0:
                flag = False
                break
        if flag:
            right_truncatable_prime_list.append(i)
    return sorted(list(set(right_truncatable_prime_list)), reverse=True)