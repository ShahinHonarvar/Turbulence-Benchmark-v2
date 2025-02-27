from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[100]
    rtp = []
    for num in range(1, x):
        if is_right_truncatable_prime(num):
            rtp.append(num)
    rtp.sort(reverse=True)
    return rtp

def is_right_truncatable_prime(num):
    while num > 0:
        if not isprime(num):
            return False
        num = int(str(num)[1:])
    return True