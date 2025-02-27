def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isTruncatable(num):
    while num != 0:
        if not isPrime(num):
            return False
        num //= 10
    return True

def all_left_truncatable_prime(t):
    leftmost_digits = [int(str(x)[-i - 1]) for i in range(len(str(t[767])) - 1, -1, -1)]
    left_truncatable_prime = []
    for i in range(1, t[767]):
        if isPrime(i) and (not '0' in str(i)) and all(isTruncatable(int(str(i).rjust(j + 1, '0')))) and (i not in left_truncatable_prime):
            left_truncatable_prime.append(i)
    return sorted(left_truncatable_prime, reverse=True)