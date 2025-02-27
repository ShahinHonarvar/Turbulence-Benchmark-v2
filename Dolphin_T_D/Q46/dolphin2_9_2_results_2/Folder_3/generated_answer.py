def gcf_three_nums(numbers):
    num1 = numbers[31]
    num2 = numbers[69]
    num3 = numbers[40]

    def gcf(num1, num2):
        while num2 != 0:
            num1, num2 = (num2, num1 % num2)
        return num1
    gcf_value = gcf(num1, num2)
    while num3 != 0:
        gcf_value, num3 = (num3, gcf_value % num3)
    return gcf_value