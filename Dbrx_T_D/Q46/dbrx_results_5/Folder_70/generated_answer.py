from fractions import gcd

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[990], numbers[671], numbers[711]]
    gcf = nums_at_indices[0]
    for num in nums_at_indices[1:]:
        gcf = gcd(gcf, num)
    return gcf