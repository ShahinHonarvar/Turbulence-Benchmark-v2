def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def left_truncatable_primes(limit):
    primes = []
    queue = [str(i) for i in range(1, 10) if is_prime(i)]
    while queue:
        num = queue.pop(0)
        num_int = int(num)
        if num_int < limit:
            primes.append(num_int)
            for next_digit in '123456789':
                next_num = next_digit + num
                if is_prime(int(next_num)):
                    queue.append(next_num)
    return primes

def all_left_truncatable_prime(tup):
    x = tup[6]
    return sorted(left_truncatable_primes(x), reverse=True)