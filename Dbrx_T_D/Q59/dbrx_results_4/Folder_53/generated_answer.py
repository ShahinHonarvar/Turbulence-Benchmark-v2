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
        i += 6
    return True

def all_left_truncatable_prime(limit):
    result = []
    for num in range(1, limit):
        num_str = str(num)[1:]
        if int(num_str) != num and is_prime(int(num_str)):
            result.append(num)
    return sorted(result, reverse=True)