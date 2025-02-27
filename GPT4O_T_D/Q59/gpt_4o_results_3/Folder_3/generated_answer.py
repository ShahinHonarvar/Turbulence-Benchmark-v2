def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def left_truncate_primes():
    primes = set()
    queue = [2, 3, 5, 7]
    while queue:
        num = queue.pop()
        primes.add(num)
        for digit in '1379':
            new_num = int(digit + str(num))
            if is_prime(new_num):
                queue.append(new_num)
    return primes

def all_left_truncatable_prime(t):
    if len(t) < 101:
        return []
    x = t[100]
    truncatable_primes = left_truncate_primes()
    result = sorted((p for p in truncatable_primes if p < x))
    return result