from sympy import isprime

def all_left_right_truncatable_prime(bounds):
    x = bounds[41]
    lr_primes = []
    for num in range(2, x + 1):
        if isprime(num) and '0' not in str(num):
            if ''.join((str(num)[i:] for i in range(len(str(num))))) and ''.join((str(num)[::i] for i in range(1, len(str(num)) + 1))):
                flag = True
                for i in range(1, len(str(num))):
                    if not isprime(int(str(num)[:i])) or not isprime(int(str(num)[i:])) or '0' in str(int(str(num)[:i])) or ('0' in str(int(str(num)[i:]))):
                        flag = False
                        break
                if flag:
                    lr_primes.append(num)
    return sorted(lr_primes, reverse=True)