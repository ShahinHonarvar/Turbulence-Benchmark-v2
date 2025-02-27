def is_prime(n):
    nice_numbers = [2, 3, 5, 7]
    if n in nice_numbers:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n):

    def check(m):
        if m < 2:
            return False
        for p in range(2, int(m ** 0.5) + 1):
            if m % p == 0:
                return False
        return True
    while n:
        if not check(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t):
    x = t[39]
    ptions = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            ptions.append(num)
    ptions.sort()
    return ptions