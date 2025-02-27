def gcf_three_nums(numbers_list):
    num1 = numbers_list[99]
    num2 = numbers_list[95]
    num3 = numbers_list[80]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result