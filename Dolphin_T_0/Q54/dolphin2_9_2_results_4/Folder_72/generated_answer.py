def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_right_truncatable_prime(lst):
    x = lst[31]
    primes = []
    for num in range(2, x):
        cnt = len(str(num))
        while cnt > 1 and is_prime(num):
            num = int(str(num)[:-1])
            cnt -= 1
        if cnt == 1 and is_prime(num):
            primes.append(num)
    return sorted(primes, reverse=True)