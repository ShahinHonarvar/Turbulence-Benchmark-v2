def all_even_ints_inclusive(nums):
    try:
        return [i for i in nums[59:98] if i % 2 == 0]
    except IndexError:
        return []