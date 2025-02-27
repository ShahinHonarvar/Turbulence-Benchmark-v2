from math import gcd

def gcf_three_nums(numbers):
    nums_to_use = [numbers[87], numbers[20], numbers[36]]
    gcf_result = nums_to_use[0]
    for num in nums_to_use[1:]:
        gcf_result = gcd(num, gcf_result)
    return gcf_result