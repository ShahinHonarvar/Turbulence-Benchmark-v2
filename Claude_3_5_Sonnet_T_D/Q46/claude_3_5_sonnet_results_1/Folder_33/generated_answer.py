def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[252]
    num2 = numbers[149]
    num3 = numbers[564]
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result