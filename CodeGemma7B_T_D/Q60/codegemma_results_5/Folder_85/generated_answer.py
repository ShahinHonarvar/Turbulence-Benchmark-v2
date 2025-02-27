def all_left_right_truncatable_prime(tup):
    x = tup[94]
    left_right_truncatable_prime = []
    for a in range(2, x + 1):
        if len(str(a)) <= 1 or '0' in str(a):
            continue
        left, right = (a, int(str(a)[::-1]))
        while left >= 2 and right >= 2:
            if left != right and left == sieve(left) and (right == sieve(right)):
                left_right_truncatable_prime.append(a)
                break
            left = int(str(left)[1:])
            right = int(str(right)[:-1])
    return sorted(left_right_truncatable_prime)

def sieve(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True