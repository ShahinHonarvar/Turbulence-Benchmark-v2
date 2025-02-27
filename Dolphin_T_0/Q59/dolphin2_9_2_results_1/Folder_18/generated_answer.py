def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(num):
    x = num[429]
    primes = []
    for i in range(x, 1, -1):
        if is_prime(i) and str(i).count('0') == 0:
            temp = i
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                primes.append(i)
    return primes