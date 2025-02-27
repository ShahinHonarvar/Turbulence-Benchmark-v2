def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def right_truncatable_prime(n):
    for i in range(n - 1, 0, -1):
        if is_prime(i):
            copy = i
            while copy > 0:
                if not is_prime(copy):
                    break
                copy //= 10
            else:
                return True
    return False

def all_right_truncatable_prime(t):
    xs = t[55]
    results = []
    for i in range(xs - 1, 0, -1):
        if right_truncatable_prime(i):
            results.append(i)
    return sorted(results, reverse=True)