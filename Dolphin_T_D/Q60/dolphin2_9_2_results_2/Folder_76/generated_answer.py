def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n == 1 or n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[370]
    truncable_primes = []
    for num in range(x, 1, -1):
        if is_prime(num) and '0' not in str(num):
            for i in range(0, len(str(num)) - 1):
                trunc = int(str(num)[i:len(str(num)) - 1])
                if not is_prime(trunc) or str(trunc).count('0') > 0:
                    break
                trunc = int(str(num)[1:])
                if not is_prime(trunc) or str(trunc).count('0') > 0:
                    break
            else:
                truncable_primes.append(num)
    return sorted(truncable_primes, reverse=True)