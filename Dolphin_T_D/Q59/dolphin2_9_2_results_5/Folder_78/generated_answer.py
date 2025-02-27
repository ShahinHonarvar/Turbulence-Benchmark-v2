def is_prime(y):
    if y == 1:
        return False
    if y == 2:
        return True
    if y % 2 == 0:
        return False
    z = 3
    while z * z <= y:
        if y % z == 0:
            return False
        z += 2
    return True

def all_left_truncatable_prime(vals):
    x = vals[23]
    truncatable_primes = []
    for y in range(2, x):
        if is_prime(y):
            str_y = str(y)
            if str_y.count('0') == 0:
                z = len(str_y)
                while z >= 1:
                    if not is_prime(int(str_y[z - 1:])):
                        break
                    z -= 1
                if z == 0:
                    truncatable_primes.append(y)
    truncatable_primes.sort()
    return truncatable_primes