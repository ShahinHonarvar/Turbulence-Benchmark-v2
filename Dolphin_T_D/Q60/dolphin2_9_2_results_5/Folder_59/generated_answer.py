def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(x):
    trunc_primes = []
    for num in range(x, 1, -1):
        if '0' in str(num):
            continue
        while num > 1 and is_prime(num):
            trunc = int(str(num)[1:-1])
            if trunc > 1 and is_prime(trunc):
                num = trunc
            else:
                break
        if num == 1:
            trunc_primes.append(num)
    return sorted(trunc_primes, reverse=True)