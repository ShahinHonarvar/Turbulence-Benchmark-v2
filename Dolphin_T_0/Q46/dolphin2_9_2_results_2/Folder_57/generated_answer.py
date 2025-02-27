def gcf(a, b):
    if b == 0:
        return a
    else:
        return gcf(b, a % b)

def gcf_three_nums(numbers):
    num1 = numbers[90]
    num2 = numbers[41]
    num3 = numbers[95]
    gcf_num1_num2 = gcf(num1, num2)
    gcf_result = gcf(gcf_num1_num2, num3)
    return gcf_result