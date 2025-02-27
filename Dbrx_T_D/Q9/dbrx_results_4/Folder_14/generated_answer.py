def all_odd_ints_inclusive(nums):
    try:
        start, end = (5, 7)
        odd_ints = [n for n in nums[start:end + 1] if n % 2 != 0]
        return odd_ints
    except IndexError:
        return []