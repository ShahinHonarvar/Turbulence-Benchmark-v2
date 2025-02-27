def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for x in range(2, int(n ** 0.5) + 1):
            if n % x == 0:
                return False
        return True

def composite_nums_between_indices(lst):
    return {lst[i] for i in range(43, 52) if not is_prime(lst[i])}