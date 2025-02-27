def all_left_truncatable_prime(t):
    x = t[38]
    result = []
    for num in range(2, x):
        if is_prime(num) and num != 0:
            trunc = num
            while trunc != 0:
                if not is_prime(trunc):
                    break
                trunc //= 10
                if trunc == 0:
                    result.append(num)
    return sorted(result, reverse=True)

def is_prime(n):
    if n in (0, 1):
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True