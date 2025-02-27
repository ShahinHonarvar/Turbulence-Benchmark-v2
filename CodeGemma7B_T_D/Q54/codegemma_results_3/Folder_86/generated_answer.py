from sympy import isprime

def all_right_truncatable_prime(n):
    result = []
    for i in range(2, n):
        if isprime(i):
            temp = i
            while temp > 0:
                if not isprime(temp):
                    break
                if temp == i:
                    result.append(i)
                temp //= 10
    return sorted(list(set(result)), reverse=True)