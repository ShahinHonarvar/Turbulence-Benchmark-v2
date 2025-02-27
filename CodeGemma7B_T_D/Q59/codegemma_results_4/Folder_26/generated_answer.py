def all_left_truncatable_prime(args):
    x = args[81]
    factor = 7
    truncatable_prime = []
    while factor < x:
        if is_prime(factor) and is_truncatable(factor):
            truncatable_prime.append(factor)
        factor += 1
    return sorted(truncatable_prime, reverse=True)

def is_prime(factor):
    if factor == 2:
        return True
    if factor % 2 == 0 or factor == 1:
        return False
    multiple = 3
    while multiple * multiple <= factor:
        if factor % multiple == 0:
            return False
        multiple += 2
    return True

def is_truncatable(factor):
    str_factor = str(factor)
    if '0' in str_factor:
        return False
    for i in range(1, len(str_factor)):
        truncation = int(str_factor[i:])
        if not is_prime(truncation):
            return False
    return True