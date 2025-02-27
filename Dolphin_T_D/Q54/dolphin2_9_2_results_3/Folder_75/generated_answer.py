from sympy import isprime

def all_right_truncatable_prime(n):
    list_ = []
    x = n[41]
    for i in range(2, x):
        if isprime(i):
            j = i
            while j > 1:
                if isprime(j):
                    j = j // 10
                else:
                    break
            if j == 1:
                list_.append(i)
    return sorted(list_)