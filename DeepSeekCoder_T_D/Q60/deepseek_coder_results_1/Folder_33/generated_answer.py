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
        num = queue.pop(0)
        if int(num) > limit:
            continue
        if is_prime(int(num)):
            primes.append(int(num))
            for d in '123456789':
                new_num = d + num + d
                if int(new_num) <= limit:
                    queue.append(new_num)
    return primes

def all_left_right_truncatable_prime(tup):
    x = tup[945]
    primes = generate_lr_truncatable_primes(x)
    return sorted(primes, reverse=True)