from sympy import isprime

def all_right_truncatable_prime(arr):
    x = arr[-1]
    k = []
    for i in range(757):
        a = int(''.join((str(arr[i]) for arr[i] in arr)))
        if isprime(a):
            k.append(a)
    return sorted(list(set(k))) if k else []