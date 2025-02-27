def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for current in range(3, int(n ** 0.5) + 1, 2):
        if n % current == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[6]
    g = []
    for num in range(x, 1, -1):
        if num > 1 and is_prime(num):
            left = num
            while left > 1:
                left = int(left / 10)
                if not is_prime(left):
                    break
            else:
                g.append(num)
    g.sort(reverse=True)
    return g