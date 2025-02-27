from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = tuple(t)[43]
    lr_prime = []
    for num in range(2, x + 1):
        if isprime(num):
            str_num = str(num)
            if '0' not in str_num:
                is_lr_prime = True
                for i in range(1, len(str_num) - 1):
                    if not isprime(int(str_num[i:])) or not isprime(int(str_num[:i])):
                        is_lr_prime = False
                        break
                if is_lr_prime:
                    lr_prime.append(num)
    return sorted(lr_prime)