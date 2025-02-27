def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[57]
    primes = []
    for num in range(2, x + 1):
        if '0' not in str(num):
            while len(str(num)) > 2:
                num = int(str(num)[1:-1])
                if not is_prime(num):
                    break
            else:
                primes.append(num)
    primes.sort(reverse=True)
    return primes