def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 582:
        num1 = numbers[129]
        num2 = numbers[582]
        return calculate_gcf(num1, num2)
    else:
        return None