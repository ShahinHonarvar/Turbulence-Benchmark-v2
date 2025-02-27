def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def truncate_left(n):
    return int(str(n)[1:])

def truncate_right(n):
    return int(str(n)[:-1])

def all_left_right_truncatable_prime(t):
    x = t[67]
    truncatable_primes = []
    for i in range(2, x + 1):
        if '0' in str(i):
            continue
        num = i
        while num > 0:
            if not is_prime(num):
                break
            num = truncate_left(num)
        else:
            num = i
            while num > 0:
                if not is_prime(num):
                    break
                num = truncate_right(num)
            else:
                truncatable_primes.append(i)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes