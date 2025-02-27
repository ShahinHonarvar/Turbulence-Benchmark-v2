def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_truncatable_prime(t):
    x = t[8]
    left_truncatable_primes = []
    for num in range(10, x):
        if is_prime(num) and '0' not in str(num):
            temp = str(num)
            is_left_truncatable = True
            for i in range(1, len(temp)):
                if not is_prime(int(temp[i:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes, reverse=True)