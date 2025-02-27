def gcf_three_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 81:
        return "List doesn't have enough elements."
    num1 = numbers[31]
    num2 = numbers[25]
    num3 = numbers[80]
    return gcf(num1, gcf(num2, num3))