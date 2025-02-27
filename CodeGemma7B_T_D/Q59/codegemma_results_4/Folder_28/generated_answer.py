def all_left_truncatable_prime(tup):
    x = tup[19]
    return sorted([y for y in range(2, x) if str(y) not in '0' and is_prime(int(str(y)[1:])) and is_prime(y)])