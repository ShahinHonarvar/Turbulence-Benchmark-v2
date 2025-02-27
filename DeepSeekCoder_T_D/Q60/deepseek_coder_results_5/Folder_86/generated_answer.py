def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_lr_truncatable_primes(limit):
    primes = []
    queue = ['2', '3', '5', '7']
    while queue:
        current = queue.pop(0)
        num = int(current)
        if num > limit:
            continue
        if is_prime(num):
            primes.append(num)
            for digit in '123456789':
                queue.append(current + digit)
                queue.append(digit + current)
    return primes

def all_left_right_truncatable_prime(t):
    if len(t) <= 126:
        return []
    x = t[126]
    lr_truncatable_primes = generate_lr_truncatable_primes(x)
    return sorted(set(lr_truncatable_primes), reverse=True)