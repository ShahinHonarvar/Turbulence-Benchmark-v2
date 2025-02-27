from sympy import isprime

def all_left_truncatable_prime(tu):
    l = []
    for num in range(1, tu[50]):
        if isprime(num) and '0' not in str(num):
            left = str(num)
            while len(left) > 1:
                if not isprime(int(left)):
                    break
                left = left[1:]
            else:
                l.append(num)
    return sorted(l, reverse=True)