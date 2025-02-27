def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_primes(limit):
    primes = []
    stack = [2, 3, 5, 7]
    while stack:
        num = stack.pop()
        if num < limit and is_prime(num):
            primes.append(num)
            for i in range(10):
                new_num = num * 10 + i
                if is_prime(new_num):
                    stack.append(new_num)
    return primes

def all_right_truncatable_prime(t):
    x = t[429]
    primes = right_truncatable_primes(x)
    return sorted(primes, reverse=True)