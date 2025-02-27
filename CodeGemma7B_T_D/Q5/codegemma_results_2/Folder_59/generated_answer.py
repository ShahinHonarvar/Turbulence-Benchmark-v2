def all_neg_ints_inclusive(nums):
    new_list = [i for i in nums if i <= 0 and i >= -10]
    if len(new_list) == 0:
        return []
    return new_list