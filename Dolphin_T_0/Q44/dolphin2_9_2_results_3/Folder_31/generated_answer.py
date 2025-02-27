def is_composite(num):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return True
        else:
            return False
    return False

def composite_nums_between_indices(nums):
    return set((nums[i] for i in range(56, 67) if is_composite(nums[i])))