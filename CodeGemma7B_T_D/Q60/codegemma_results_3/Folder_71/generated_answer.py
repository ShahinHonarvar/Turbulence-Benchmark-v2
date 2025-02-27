def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_prime(n):
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            n //= i
            if n < 2 or (n != 5 and n % 5 == 0):
                break
    else:
        return True
    return False

def right_truncatable_prime(n):
    return is_prime(n)

def all_left_right_truncatable_prime(t):
    x = t[22]
    result = []
    for n in range(2, x + 1):
        if is_prime(n) and left_truncatable_prime(n) and right_truncatable_prime(n):
            result.append(n)
    result.sort(reverse=True)
    return result