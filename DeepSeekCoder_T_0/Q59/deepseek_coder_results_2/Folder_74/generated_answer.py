def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []
    queue = ['']
    while queue:
        current = queue.pop(0)
        for digit in '123456789':
            num = int(digit + current)
            if num >= limit:
                continue
            if is_prime(num):
                queue.append(str(num))
                if '0' not in str(num):
                    primes.append(num)
    return sorted(primes)

def all_left_truncatable_prime(tup):
    x = tup[36]
    return left_truncatable_primes(x)