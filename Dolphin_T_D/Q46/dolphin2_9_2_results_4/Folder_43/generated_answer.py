def gcf_three_nums(numbers):
    num1 = numbers[33]
    num2 = numbers[78]
    num3 = numbers[93]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(num1, num2), num3)