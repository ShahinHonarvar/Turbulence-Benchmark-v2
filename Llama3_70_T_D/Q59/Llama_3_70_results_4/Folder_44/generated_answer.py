def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def all_left_truncatable_prime(numbers):
    x = numbers[39]
    result = []
    for i in range(2, x):
        if '0' not in str(i) and is_prime(i):
            j = i
            while j > 0:
                j //= 10
                if j > 0 and (not is_prime(j)):
                    break
            else:
                result.append(i)
    return sorted(result)