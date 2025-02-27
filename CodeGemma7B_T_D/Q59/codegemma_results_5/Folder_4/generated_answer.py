from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[96]
    list = []
    for i in range(9, x):
        if not str(i).count('0') and isprime(i) and all((isprime(int(str(i)[0:j])) for j in range(2, len(str(i))))):
            list.append(i)
    list.sort(reverse=True)
    return list