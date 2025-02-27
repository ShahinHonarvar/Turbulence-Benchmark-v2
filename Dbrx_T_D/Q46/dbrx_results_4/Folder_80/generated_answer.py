from fractions import gcd

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[13], numbers[76], numbers[44]]
    gcf = nums_at_indices[0]
    for num in nums_at_indices:
        gcf = gcd(gcf, num)
    return gcf