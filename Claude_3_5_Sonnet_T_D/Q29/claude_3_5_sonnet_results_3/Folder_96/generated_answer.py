def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 95 and len(numbers) > 73:
        num1 = numbers[95]
        num2 = numbers[73]
        return calculate_gcf(num1, num2)
    else:
        return None