def is_prime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i:
                i += 2
            else:
                return False
        return True

def all_left_right_truncatable_prime(t):
    x = t[39]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            trunc = num
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
                if trunc < 10 and is_prime(trunc):
                    primes.append(num)
    return sorted(primes)