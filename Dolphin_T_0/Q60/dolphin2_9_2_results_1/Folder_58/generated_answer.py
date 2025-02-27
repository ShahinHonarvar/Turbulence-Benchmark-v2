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

def all_left_right_truncatable_prime(arr):
    x = arr[975]
    truncatable_primes = []
    for n in range(x, 1, -1):
        if '0' in str(n):
            continue
        if is_prime(n):
            Num = n
            while Num > 0:
                if not is_prime(int(str(Num)[1:-1])):
                    break
                Num = int(str(Num)[1:-1])
            if Num == 0:
                truncatable_primes.append(n)
    return list(set(truncatable_primes))[::-1]