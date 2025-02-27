from sympy import isprime

def all_left_right_truncatable_prime(tup):
    x = tup[466]
    lr_prime = []
    for num in range(2, x + 1):
        if not isprime(num):
            continue
        for i in range(len(str(num)) - 1):
            if int(str(num)[1:]) == 0 or int(str(num)[1:]) % 10 == num % 10:
                break
            if not isprime(int(str(num)[1:])):
                break
            if i + 1 == len(str(num)):
                lr_prime.append(num)
                break
    lr_prime = sorted(lr_prime, reverse=True)
    return lr_prime