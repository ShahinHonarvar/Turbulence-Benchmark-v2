def is_prime(n):
    if n in (0, 1):
        return False
    elif n in (2, 3):
        return True
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

def all_left_truncatable_prime(integer_tuple):
    x = integer_tuple[784]
    prim_list = [i for i in range(2, x) if is_prime(i)]
    res = [i for i in prim_list if all((is_prime(int(str(i)[j:])) for j in range(1, len(str(i)))))]
    return sorted(res)