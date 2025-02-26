def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 42 and len(numbers) > 25:
        num1 = numbers[42]
        num2 = numbers[25]
        return calculate_gcf(num1, num2)
    else:
        return None