def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate_number(n):
    str_n = str(n)
    length = len(str_n)
    truncations = set()
    for i in range(length):
        left_trunc = int(str_n[i:]) if str_n[i:] else None
        right_trunc = int(str_n[:length - i]) if str_n[:length - i] else None
        if left_trunc:
            truncations.add(left_trunc)
        if right_trunc:
            truncations.add(right_trunc)
    return truncations

def all_left_right_truncatable_prime(numbers):
    x = numbers[0]
    result = []
    for n in range(2, x + 1):
        if '0' in str(n):
            continue
        truncations = truncate_number(n)
        if all((is_prime(t) for t in truncations)):
            result.append(n)
    return sorted(result, reverse=True)