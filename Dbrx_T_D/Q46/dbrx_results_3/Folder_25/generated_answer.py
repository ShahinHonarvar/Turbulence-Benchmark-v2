from fractions import gcd

def gcf_three_nums(numbers):
    index_numbers = [numbers[32], numbers[54], numbers[13]]
    gcf = index_numbers[0]
    for num in index_numbers:
        gcf = gcd(gcf, num)
    return gcf