def all_neg_ints_exclusive(nums):
    neg_indices = [i for i, num in enumerate(nums) if num < 0]
    filtered_indices = [i for i in neg_indices if 81 <= i < 86]
    return [nums[i] for i in filtered_indices]