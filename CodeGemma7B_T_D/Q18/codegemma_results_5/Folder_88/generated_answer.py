import itertools

def sum_ints_div_by_either_nums(nums):
    sum_ = 0
    for i in itertools.islice(nums, 3, 10):
        if i % 6 == 0 or i % 1 == 0:
            sum_ += i
    return sum_