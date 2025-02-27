def gcf_three_nums(numbers):
    num1 = numbers[742]
    num2 = numbers[888]
    num3 = numbers[629]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(num1, gcf(num2, num3))