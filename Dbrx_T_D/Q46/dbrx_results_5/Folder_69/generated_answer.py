def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_to_check = [numbers[404], numbers[834], numbers[517]]
    greatest_common_factor = nums_to_check[0]
    for num in nums_to_check:
        greatest_common_factor = gcd(greatest_common_factor, num)
    return greatest_common_factor