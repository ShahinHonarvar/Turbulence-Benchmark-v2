def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []
    queue = ['2', '3', '5', '7']
    while queue:
        num_str = queue.pop(0)
        num = int(num_str)
        if num >= limit:
            continue
        if is_prime(num):
            primes.append(num)
            for digit in '123456789':
                new_num_str = digit + num_str
                queue.append(new_num_str)
    return primes

def all_left_truncatable_prime(tup):
    x = tup[760]
    primes = left_truncatable_primes(x)
    return sorted(primes, reverse=True)