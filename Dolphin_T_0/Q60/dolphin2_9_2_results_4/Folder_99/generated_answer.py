def all_left_right_truncatable_prime(x):
    left_right_truncatable_prime = []
    for i in range(2, x):
        if is_prime(i):
            left_OK = True
            while i != 0 and i != 1 and left_OK:
                left_OK &= is_prime(i)
                i //= 10
            right_OK = True
            j = i
            while j != 0 and j != 1 and right_OK:
                right_OK &= is_prime(j)
                j %= 100
                j //= 10
            if left_OK and right_OK:
                left_right_truncatable_prime.append(i)
    return sorted(left_right_truncatable_prime)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True