def all_odd_ints_inclusive(nums):
    all_odd = [num for num in nums[686:987 + 1] if num % 2 == 1]
    if not all_odd:
        return []
    return all_odd