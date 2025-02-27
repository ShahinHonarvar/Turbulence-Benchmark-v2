from sympy import isprime

def all_left_right_truncatable_prime(tuple):
    l = [num for num in tuple if isprime(num) and '0' not in str(num)]
    for num in l:
        for l in range(1, len(str(num))):
            if not isprime(int(str(num)[l:])):
                break
            for r in range(1, len(str(num))):
                if not isprime(int(str(num)[:-r])):
                    break
        else:
            if int(str(num)[:2]) <= 10 and num != 2:
                continue
            result.append(int(str(num)[:2]))