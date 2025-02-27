def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[86]
    left_truncatables = []
    for n in range(x - 1, 1, -1):
        if is_prime(n):
            tmp = n
            while tmp > 0:
                if not is_prime(tmp):
                    break
                tmp //= 10
            else:
                left_truncatables.append(n)
    left_truncatables.sort(reverse=True)
    return left_truncatables