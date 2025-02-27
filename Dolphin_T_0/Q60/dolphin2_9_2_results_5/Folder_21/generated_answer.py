def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(integers):
    x = integers[175]
    primes = []
    for i in range(2, x + 1):
        if i % 10 != 0 and is_prime(i):
            if i < 10:
                primes.append(i)
            else:
                trunc_left = i // 10
                trunc_right = i % 10
                while trunc_left >= 10 or trunc_right >= 10:
                    if not is_prime(trunc_left) or not is_prime(trunc_right):
                        break
                    trunc_left //= 10
                    trunc_right //= 10
                else:
                    primes.append(i)
    return sorted(primes)