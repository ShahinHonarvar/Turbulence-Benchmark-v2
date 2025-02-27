def all_right_truncatable_prime(t):
    lst = []
    for i in range(t[14]):
        if is_prime(i):
            if is_right_truncatable_prime(i):
                lst.append(i)
    lst.sort()
    return lst

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):
    last_digit = n % 10
    while n > 0:
        if is_prime(n):
            n //= 10
            last_digit = n % 10
        else:
            return False
    return True