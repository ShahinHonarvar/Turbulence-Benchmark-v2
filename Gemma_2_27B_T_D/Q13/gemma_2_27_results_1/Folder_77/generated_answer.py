def find_second_largest_num(nums):
    try:
        return sorted(nums[527:539])[-2]
    except IndexError:
        return None