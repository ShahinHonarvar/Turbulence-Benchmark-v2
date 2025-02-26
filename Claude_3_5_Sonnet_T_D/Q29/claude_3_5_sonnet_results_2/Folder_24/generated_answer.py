def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 84 and len(numbers) > 21:
        num1 = numbers[84]
        num2 = numbers[21]
        return gcf(num1, num2)
    else:
        return None