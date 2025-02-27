from math import gcd

def gcf_three_nums(numbers):
    nums_at_indices = [numbers[34], numbers[38], numbers[77]]
    gcf = nums_at_indices[0]
    for num in nums_at_indices[1:]:
        gcf = gcd(num, gcf)
    return gcf