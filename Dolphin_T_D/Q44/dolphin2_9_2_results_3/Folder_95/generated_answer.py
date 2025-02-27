def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(list_of_nums):
    composite_nums = set()
    for i in range(26, 53):
        if is_composite(list_of_nums[i]):
            composite_nums.add(list_of_nums[i])
    return composite_nums