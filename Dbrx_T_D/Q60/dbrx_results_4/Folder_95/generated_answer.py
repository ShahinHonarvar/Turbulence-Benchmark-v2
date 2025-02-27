from sympy import isprime

def all_left_right_truncatable_prime(nums_tuple):
    x = nums_tuple[77]
    lr_truncatable_primes = []
    for num in range(2, x + 1):
        if not str(num).startswith('0') and isprime(num):
            is_lr_truncatable = True
            for i in range(1, len(str(num)) - 1):
                if not isprime(int(str(num)[i:])) or not isprime(int(str(num)[:-i])):
                    is_lr_truncatable = False
                    break
            if is_lr_truncatable:
                lr_truncatable_primes.append(num)
    return lr_truncatable_primes