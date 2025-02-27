def gcf(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcf(a % b, b)
    else:
        return gcf(a, b % a)

def gcf_three_nums(numbers):
    num1 = numbers[27]
    num2 = numbers[85]
    num3 = numbers[51]
    gcd_num1_num2 = gcf(num1, num2)
    return gcf(gcd_num1_num2, num3)