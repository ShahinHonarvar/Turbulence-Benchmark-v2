def composite_nums_between_indices(nums):
    return {num for idx, num in enumerate(nums, 1) if 28 <= idx <= 38 and (not all((num % i for i in range(2, int(num ** 0.5) + 1))))}