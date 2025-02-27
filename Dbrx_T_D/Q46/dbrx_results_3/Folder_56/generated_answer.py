def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    nums_to_check = [numbers[59], numbers[93], numbers[84]]
    return gcd(nums_to_check[0], gcd(nums_to_check[1], nums_to_check[2]))