import math

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[36], numbers[85], numbers[83]]
    common_factors = []
    for i in range(1, min(nums_at_indices) + 1):
        if all((num % i == 0 for num in nums_at_indices)):
            common_factors.append(i)
    return max(common_factors)