from sympy import isprime

def all_left_right_truncatable_prime(x):
    a = list()
    for i in range(2, x + 1):
        b = str(i)
        if b.count('0') == 0 and b.isdigit():
            for j in list(b):
                if int(j) % 2 == 0 or int(j) == 5:
                    break
                if isprime(i):
                    a.append(i)
    return a