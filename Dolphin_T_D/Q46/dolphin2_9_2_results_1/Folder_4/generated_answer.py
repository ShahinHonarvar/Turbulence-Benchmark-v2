def gcf_three_nums(numbers):
    num1 = numbers[24]
    num2 = numbers[25]
    num3 = numbers[80]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    result = gcf(num1, num2)
    result = gcf(result, num3)
    return result