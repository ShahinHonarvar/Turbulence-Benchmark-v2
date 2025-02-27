def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 2
    return True

def left_truncatable_primes(limit):
    result = []
    for num in range(10, limit):
        if is_prime(num):
            is_left_truncatable = True
            for j in range(1, len(str(num))):
                if not is_prime(int(str(num)[j:])):
                    is_left_truncatable = False
                    break
            if is_left_truncatable:
                result.append(num)
    return sorted(result, reverse=True)

def all_left_truncatable_prime(x_tuple):
    x = x_tuple[97]
    return left_truncatable_primes(x) if x > 0 and is_prime(x) else []