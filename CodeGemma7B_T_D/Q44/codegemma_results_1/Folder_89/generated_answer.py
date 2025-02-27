def composite_nums_between_indices(nums):
    composites = {num for num in nums[36:47] if num % 2 == 1 and all((num % i != 0 for i in range(3, int(num ** 0.5) + 1, 2)))}
    return composites