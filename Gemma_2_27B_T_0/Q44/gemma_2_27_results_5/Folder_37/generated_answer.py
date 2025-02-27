def composite_nums_between_indices(nums):
    return {num for i, num in enumerate(nums[:6]) if i <= 5 and num > 1 and all((num % j for j in range(2, int(num ** 0.5) + 1)))}