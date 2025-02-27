import itertools

def sum_even_ints_inclusive(nums):
    even_nums = list(itertools.islice(filter(lambda x: x % 2 == 0, nums), 40, 81))
    if not even_nums:
        return 0
    return sum(even_nums)