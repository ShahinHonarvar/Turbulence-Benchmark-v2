def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(n):
    result = []
    nstr = str(n)
    if nstr.count('0') > 0:
        return result
    for i in range(len(nstr) - 2):
        num = int(nstr[:i + 1])
        if is_prime(num):
            result.append(num)
    return result

def right_truncatable_primes(n):
    result = []
    nstr = str(n)
    if nstr.count('0') > 0:
        return result
    for i in range(1, len(nstr)):
        num = int(nstr[i:])
        if is_prime(num):
            result.append(num)
    return result

def all_left_right_truncatable_prime(tup):
    x = tup[39]
    result = []
    for num in range(2, x + 1):
        if is_prime(num):
            left = left_truncatable_primes(num)
            right = right_truncatable_primes(num)
            if left and right:
                result.append(num)
    return sorted(result)