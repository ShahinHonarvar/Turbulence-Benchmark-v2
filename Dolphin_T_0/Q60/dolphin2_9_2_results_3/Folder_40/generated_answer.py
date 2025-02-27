from sympy import isprime

def all_left_right_truncatable_prime(X):
    x = X[10]
    lr_trunc_primes = []
    for i in range(x, 1, -1):
        if isprime(i):
            digits = [int(d) for d in str(i)]
            while digits:
                if digits[0] == 0 or digits[-1] == 0:
                    break
                else:
                    new_num = int(''.join(map(str, digits[1:-1])))
                    if new_num < 2:
                        break
                    elif isprime(new_num):
                        lr_trunc_primes.append(i)
                        break
                digits = [int(d) for d in str(new_num)]
    return sorted(lr_trunc_primes, reverse=True)