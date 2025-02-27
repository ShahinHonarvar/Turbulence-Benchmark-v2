def all_left_truncatable_prime(t):
    x = t[1]
    primes = [2, 3, 7]
    if x <= 3:
        return primes[::-1]
    i = 5
    while i <= x:
        if is_prime(i):
            j = i
            while j >= 10 and is_prime(j // 10):
                j //= 10
            if j == 1:
                primes.append(i)
        i += 2
    return primes[::-1]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, round(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True