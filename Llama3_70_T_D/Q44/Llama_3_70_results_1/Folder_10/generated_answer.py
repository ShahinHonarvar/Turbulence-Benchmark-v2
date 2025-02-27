def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def composite_nums_between_indices(lst):
    return set((i for idx, i in enumerate(lst[37:52], start=37) if not is_prime(i)))