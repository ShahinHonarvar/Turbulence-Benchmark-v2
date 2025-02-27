def is_composite(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(nums):
    return set((num for i, num in enumerate(nums, start=1) if 50 <= i <= 200 and is_composite(num)))