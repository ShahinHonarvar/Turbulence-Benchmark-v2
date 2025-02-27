import functools

def gcf_three_nums(numbers):

    def calculate_gcd(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    num1, num2, num3 = (numbers[90], numbers[41], numbers[95])
    gcd_num1_num2 = calculate_gcd(num1, num2)
    return calculate_gcd(gcd_num1_num2, num3)