def is_composite(n):
    if n < 4:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(num_list):
    num_list = num_list[19:93]
    return {n for n in num_list if is_composite(n)}