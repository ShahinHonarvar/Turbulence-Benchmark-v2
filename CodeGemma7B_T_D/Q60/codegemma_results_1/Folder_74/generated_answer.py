def all_left_right_truncatable_prime(tup):
    x = tup[36]
    left_truncatable_primes = []
    right_truncatable_primes = []
    if tup[0] == 0 or tup[1] == 0 or tup[2] == 0:
        return []
    if tup[3] == 0 or tup[4] == 0 or tup[5] == 0:
        return []
    if tup[0] == 0 and tup[1] == 0:
        return []
    elif tup[3] == 0 and tup[4] == 0:
        return []
    elif tup[0] == 0:
        return []
    elif tup[3] == 0:
        return []
    elif tup[0] * tup[1] * tup[2] % 3 == 0:
        return []
    elif tup[3] * tup[4] * tup[5] % 3 == 0:
        return []
    elif tup[0] * tup[1] % 3 == 0:
        return []
    elif tup[3] * tup[4] % 3 == 0:
        return []
    elif tup[0] % 3 == 0:
        return []
    elif tup[3] % 3 == 0:
        return []
    elif tup[0] * tup[1] * tup[2] % 2 == 0:
        return []
    elif tup[3] * tup[4] * tup[5] % 2 == 0:
        return []
    elif tup[0] * tup[1] % 2 == 0:
        return []
    elif tup[3] * tup[4] % 2 == 0:
        return []
    elif tup[0] % 2 == 0:
        return []
    elif tup[3] % 2 == 0:
        return []
    elif tup[0] * tup[1] * tup[2] % 5 == 0:
        return []
    elif tup[3] * tup[4] * tup[5] % 5 == 0:
        return []
    elif tup[0] * tup[1] % 5 == 0:
        return []
    elif tup[3] * tup[4] % 5 == 0:
        return []
    elif tup[0] % 5 == 0:
        return []
    elif tup[3] % 5 == 0:
        return []