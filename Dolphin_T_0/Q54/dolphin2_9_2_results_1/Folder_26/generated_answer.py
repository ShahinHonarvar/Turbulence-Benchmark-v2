def all_right_truncatable_prime(t):
    x = t[81]
    primes = []
    for num in range(2, x):
        if is_prime(num):
            truncate = True
            temp = num
            while temp > 1:
                temp //= 10
                if is_prime(temp):
                    truncate = True
                else:
                    truncate = False
                    break
            if truncate:
                primes.append(num)
    return sorted(primes, reverse=True)

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True