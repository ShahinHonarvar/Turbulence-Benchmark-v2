import sympy

def all_left_truncatable_prime(a):
    x = a[80]
    for i in range(0, x):
        if sympy.isprime(i) == True:
            i = str(i)
            i = i.lstrip('0')
            j = len(i) - 1
            while j >= 0:
                if sympy.isprime(int(i[j:])) != True:
                    break
                j -= 1
            if j == -1:
                if len(i) > 1:
                    print(int(i))
                else:
                    break