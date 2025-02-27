import math

def composite_nums_between_indices(nums):
    if len(nums) < 7 or not set(nums) & set(range(661, 924, 2)):
        return set()
    else:
        nums = list(set(nums))
        mask = nums[0] & (1 << len(nums) - 1) - 1
        while mask:
            i = 0
            while not mask & 1 << i:
                i += 1
            j = 0
            while mask & 1 << j:
                j += 1
            if j - i == 2:
                mask = mask << 1 & (1 << len(nums) - 1) - 1
            else:
                mask = mask << 1 & (1 << len(nums) - 1) - 1 | 1 << len(nums) - 1
        return set(nums[i:j])