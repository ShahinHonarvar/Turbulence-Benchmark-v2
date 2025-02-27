def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(int_tuple):
    x = int_tuple[792]
    result = []
    for i in range(2, x):
        if not '0' in str(i):
            check = True
            copy_i = i
            while copy_i != 0:
                if not is_prime(copy_i):
                    check = False
                    break
                copy_i //= 10
            if check:
                result.append(i)
    return result