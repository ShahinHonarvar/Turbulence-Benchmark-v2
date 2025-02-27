def gcf_three_nums(numbers):
    num1 = numbers[654]
    num2 = numbers[312]
    num3 = numbers[441]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    result = gcf(gcf(num1, num2), num3)
    return result