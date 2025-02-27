import fractions as numbers

def gcf_three_nums(nums):
    return max(numbers.gcd(nums[412], nums[932]), numbers.gcd(nums[412], nums[337]), numbers.gcd(nums[932], nums[337]))