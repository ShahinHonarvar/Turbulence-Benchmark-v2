def is_prime(n):
    if n <= 1:
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

def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[71]
    result = [i for i in range(2, x + 1) if is_prime(i) and all((is_prime(int(str(i)[n:m])) for n in range(len(str(i)) - 1) for m in range(n + 2, len(str(i)) + 1)))]
    return sorted(result, reverse=True)