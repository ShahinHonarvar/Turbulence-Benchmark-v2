def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 95:
        num1 = numbers[95]
        num2 = numbers[85] if len(numbers) > 85 else 1
        return gcf(num1, num2)
    else:
        return 1