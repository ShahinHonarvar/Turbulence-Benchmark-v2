from sympy import isprime

def all_left_right_truncatable_prime(bounds):
    lower, upper = bounds
    lr_primes = []
    for num in range(lower, upper + 1):
        if isprime(num) and (not '0' in str(num)):
            num_str = str(num)
            is_lr_prime = True
            for i in range(1, len(num_str)):
                if not isprime(int(num_str[i:])):
                    is_lr_prime = False
                    break
                if not isprime(int(num_str[:-i])):
                    is_lr_prime = False
                    break
            if is_lr_prime:
                lr_primes.append(num)
    return sorted(lr_primes)