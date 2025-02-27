def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[784]
    primes = []
    for num in range(2, x):
        if '0' not in str(num) and is_prime(num):
            temp = num
            while temp != 0:
                if not is_prime(temp):
                    break
                temp //= 10
                if temp == 0:
                    primes.append(num)
    return sorted(primes)