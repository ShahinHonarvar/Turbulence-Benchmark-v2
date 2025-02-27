def all_odd_ints_inclusive(nums):
    try:
        start, end = (246, 750)
        odd_ints = [num for num in nums[start:end + 1] if num % 2 != 0]
        return odd_ints
    except IndexError:
        return []