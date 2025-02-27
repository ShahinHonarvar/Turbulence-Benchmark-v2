import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(tup):
    x = tup[14]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num):
            cont = True
            n = num
            while n > 9:
                n = n // 10
                if not is_prime(n):
                    cont = False
                    break
            if cont:
                rev_num = int(str(num)[::-1])
                if is_prime(rev_num):
                    primes.append(num)
    return sorted(primes)