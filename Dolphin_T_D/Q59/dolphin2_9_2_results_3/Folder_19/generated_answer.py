def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_truncatable(num, x):
    num = str(num)
    x = str(x)
    for i in range(len(num)):
        if num[:i + 1] == x[:i + 1]:
            return True
    return False

def all_left_truncatable_prime(x):
    primes = [2, 3, 5, 7]
    num = 11
    while num < x:
        if is_prime(num) and is_truncatable(num, x):
            primes.append(num)
        num += 2
    primes.sort(reverse=True)
    return primes