from sympy import prime

def all_left_truncatable_prime(x):
    result = []
    for p in range(2, x):
        if not '0' in str(p):
            truncatable = True
            for i in range(1, len(str(p))):
                if not prime(int(str(p)[i:])):
                    truncatable = False
                    break
            if truncatable:
                result.append(p)
    return sorted(result)