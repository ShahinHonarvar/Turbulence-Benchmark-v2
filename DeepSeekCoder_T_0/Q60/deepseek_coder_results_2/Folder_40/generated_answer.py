def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(t):
    x = t[10]
    primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        all_prime = True
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:len(str(num)) - i])):
                all_prime = False
                break
        if all_prime:
            primes.append(num)
    return sorted(primes, reverse=True)