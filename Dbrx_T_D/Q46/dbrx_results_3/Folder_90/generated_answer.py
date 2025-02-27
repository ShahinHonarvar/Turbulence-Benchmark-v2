from math import gcd

def gcf_three_nums(numbers):
    nums_to_consider = [numbers[818], numbers[606], numbers[873]]
    gcf = nums_to_consider[0]
    for num in nums_to_consider:
        gcf = gcd(gcf, num)
    return gcf