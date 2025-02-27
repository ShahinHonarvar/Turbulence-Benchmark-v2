import math

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[145], numbers[183], numbers[770]]
    common_factors = []
    for i in range(1, math.floor(min(nums_to_consider))):
        factor_found = True
        for num in nums_to_consider:
            if num % i != 0:
                factor_found = False
                break
        if factor_found:
            common_factors.append(i)
    return max(common_factors) if common_factors else 1