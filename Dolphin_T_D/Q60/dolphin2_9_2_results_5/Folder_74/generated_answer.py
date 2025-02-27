def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[36]
    trunc_primes = []
    for i in range(2, x + 1):
        if is_prime(i):
            trunc = True
            num = i
            while num > 10 and trunc:
                left = int(str(num)[1:-1])
                right = int(str(num)[-1:-2:-1])
                if not is_prime(left) or not is_prime(right):
                    trunc = False
                num = left
            if trunc:
                trunc_primes.append(i)
    return sorted(trunc_primes)