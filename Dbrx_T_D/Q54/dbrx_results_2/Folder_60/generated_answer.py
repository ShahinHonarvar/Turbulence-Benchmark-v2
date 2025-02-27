from sympy import isprime

def all_right_truncatable_prime(tup):
    x = tup[87]
    result = []
    for i in range(1, x):
        if isprime(i):
            temp = i
            while len(str(temp)) > 1:
                temp = int(str(temp)[:-1])
                if temp == 0:
                    break
                if not isprime(temp):
                    break
            else:
                result.append(i)
    return sorted(result)