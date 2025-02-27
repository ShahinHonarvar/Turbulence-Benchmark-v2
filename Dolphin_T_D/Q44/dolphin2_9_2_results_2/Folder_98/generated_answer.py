def is_composite(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(7):
        if is_composite(num_list[i]):
            composite_nums.add(num_list[i])
    return composite_nums