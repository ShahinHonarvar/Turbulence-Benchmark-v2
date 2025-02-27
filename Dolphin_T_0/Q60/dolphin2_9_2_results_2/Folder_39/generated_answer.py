def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[30]
    truncatable_primes = []
    for i in range(x, 0, -1):
        if is_prime(i) and '0' not in str(i):
            n = i
            while n not in [2, 3]:
                n = (int(''.join(filter(str.isdigit, str(n)))), int(''.join(reversed(filter(str.isdigit, str(n))))))
                if not (is_prime(n[0]) and is_prime(n[1])):
                    break
            else:
                truncatable_primes.append(i)
    return sorted(truncatable_primes, reverse=True)