def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums) if 80 <= i <= 200 and num > 1 and (not all((num % j for j in range(2, int(num ** 0.5) + 1))))}