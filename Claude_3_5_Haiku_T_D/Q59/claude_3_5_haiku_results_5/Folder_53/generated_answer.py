def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[86]
    result = []
    for num in range(x - 1, 1, -1):
        if '0' not in str(num):
            truncatable = True
            truncated = num
            while len(str(truncated)) > 1:
                truncated = int(str(truncated)[1:])
                if not is_prime(truncated):
                    truncatable = False
                    break
            if truncatable and is_prime(num):
                result.append(num)
    return sorted(result, reverse=True)