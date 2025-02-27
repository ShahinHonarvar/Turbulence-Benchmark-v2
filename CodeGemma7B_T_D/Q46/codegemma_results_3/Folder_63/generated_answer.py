def gcf_three_nums(numbers):
    num1 = numbers[38]
    num2 = numbers[52]
    num3 = numbers[69]
    gcf = gcf(num1, num2)
    gcf = gcf(gcf, num3)
    return gcf