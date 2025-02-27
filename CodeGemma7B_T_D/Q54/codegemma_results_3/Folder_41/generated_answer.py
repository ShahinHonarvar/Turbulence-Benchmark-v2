from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[46]
    l = []
    for i in range(x):
        if isprime(i) and (i // 10 ** j % 10 ** j not in [0, 2, 4, 5, 6, 8] or (i // 10 ** j % 10 in [2, 3, 5, 7, 8] and i // 10 ** (j + 1) % 100 in [11, 37, 43, 67, 71, 73, 97])):
            l.append(i)
    l.sort(reverse=True)
    return l