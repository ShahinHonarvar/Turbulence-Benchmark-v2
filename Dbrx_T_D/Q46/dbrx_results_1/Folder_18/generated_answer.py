import math

def gcf_three_nums(numbers):
    nums_to_check = [numbers[637], numbers[411], numbers[757]]
    gcf = math.gcd(nums_to_check[0], nums_to_check[1])
    for num in nums_to_check[2:]:
        gcf = math.gcd(gcf, num)
    return gcf