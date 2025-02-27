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

def all_left_right_truncatable_prime(t):
    x = t[175]
    trunc_primes = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if is_prime(num):
            flag = True
            for i in range(1, len(str(num))):
                if not is_prime(int(str(num)[i:])) or not is_prime(int(str(num)[:-i])):
                    flag = False
                    break
            if flag:
                trunc_primes.append(num)
    return sorted(trunc_primes)