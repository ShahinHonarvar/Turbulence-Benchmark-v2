import sympy

def all_left_truncatable_prime(arguments):
    x = arguments[86]
    left_truncatable_primes = []
    for i in range(x, 1, -1):
        if sympy.isprime(i):
            number_string = str(i)
            if '0' in number_string:
                continue
            else:
                continue_flag = True
                for j in range(len(number_string)):
                    if sympy.isprime(int(number_string[j:])):
                        next
                    else:
                        continue_flag = False
                        break
                if continue_flag:
                    left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes, reverse=True)