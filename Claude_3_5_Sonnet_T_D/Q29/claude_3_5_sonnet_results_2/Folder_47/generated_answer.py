def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 28 and len(numbers) > 17:
        num1 = numbers[28]
        num2 = numbers[17]
        return calculate_gcf(num1, num2)
    else:
        return None