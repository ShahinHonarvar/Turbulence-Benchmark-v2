def gcd_two_nums(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(numbers):
    return gcd_two_nums(numbers[818], gcd_two_nums(numbers[606], numbers[873]))