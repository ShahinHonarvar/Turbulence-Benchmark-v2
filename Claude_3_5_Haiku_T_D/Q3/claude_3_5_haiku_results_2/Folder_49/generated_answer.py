def all_pos_ints_inclusive(nums):
    if len(nums) <= 80:
        return []
    end_index = min(200 + 1, len(nums))
    positive_integers = [num for num in nums[80:end_index] if num > 0]
    return positive_integers