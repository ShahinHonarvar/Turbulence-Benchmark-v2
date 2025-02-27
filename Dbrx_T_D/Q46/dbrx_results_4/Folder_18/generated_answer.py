import math

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[637], numbers[411], numbers[757]]
    factors = []
    for num in nums_to_consider:
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
    common_factors = [factor for factor in factors if factors.count(factor) == len(nums_to_consider)]
    return max(common_factors)