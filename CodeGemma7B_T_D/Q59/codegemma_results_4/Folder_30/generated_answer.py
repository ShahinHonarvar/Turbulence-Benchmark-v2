import sympy as sp

def all_left_truncatable_prime(tuple):
    prime = [p for p in sympy.primerange(0, tuple[37])]
    prime_set = set(prime)
    result = []
    for i in prime:
        num = str(i)
        for j in range(1, len(num)):
            if int(num[j:]) in prime_set and int(num[0:j]) in prime_set:
                result.append(i)
                break
    return list(set(sorted(result, reverse=True)))