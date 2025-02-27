def all_odd_ints_exclusive(nums):
    try:
        all_odd = [i for i in nums[743:867] if i % 2]
        return all_odd
    except IndexError:
        return []