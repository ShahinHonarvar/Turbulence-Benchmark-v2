def composite_nums_between_indices(int_list):
    composite_nums = set()
    for i in range(23, 24):
        if not is_prime(int_list[i]):
            composite_nums.add(int_list[i])
    return composite_nums

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True