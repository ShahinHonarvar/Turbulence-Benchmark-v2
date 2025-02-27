def all_left_right_truncatable_prime(numbers_tuple):
    x = numbers_tuple[79]
    primes = []
    for i in range(2, x + 1):
        if i.is_prime() and i > 9 and i.no_zero():
            if i.right_truncatable() and i.left_truncatable():
                primes.append(i)
    return primes

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def right_truncatable(n):
    num_str = str(n)
    for i in range(len(num_str) - 2, -1, -1):
        if not is_prime(int(num_str[i:])):
            return False
    return True

def left_truncatable(n):
    num_str = str(n)
    for i in range(0, len(num_str) - 1):
        if not is_prime(int(num_str[:i + 1])):
            return False
    return True

def no_zero(n):
    num_str = str(n)
    if '0' in num_str:
        return False
    return True