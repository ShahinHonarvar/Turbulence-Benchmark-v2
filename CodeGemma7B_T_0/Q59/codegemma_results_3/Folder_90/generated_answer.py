def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tup):
    x = tup[466]
    result = []
    for i in range(2, x):
        if is_prime(i) and '0' not in str(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                result.append(i)
    return sorted(result, reverse=True)