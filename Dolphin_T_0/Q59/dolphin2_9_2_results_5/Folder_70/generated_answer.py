def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0:
            return False
        if n % (f + 2) == 0:
            return False
        f += 6
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[433]
    trunc_primes = []
    for i in range(2, x):
        if is_prime(i) and str(i).count('0') == 0:
            trunc_num = i
            while trunc_num > 1:
                trunc_num = int(str(trunc_num)[1:])
                if trunc_num == 1 or not is_prime(trunc_num):
                    break
            else:
                trunc_primes.append(i)
    return sorted(trunc_primes, reverse=True)