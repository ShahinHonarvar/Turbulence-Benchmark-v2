def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_right_truncatable_prime(t):
    x = t[8]
    result = []
    for i in range(x):
        if is_prime(i):
            j = i
            while j > 0:
                if not is_prime(j):
                    break
                j = j // 10
            else:
                result.append(i)
    return sorted(result, reverse=True) if result else []