def gcf(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(numbers):
    num1 = numbers[56]
    num2 = numbers[88]
    num3 = numbers[51]
    return gcf(gcf(num1, num2), num3)