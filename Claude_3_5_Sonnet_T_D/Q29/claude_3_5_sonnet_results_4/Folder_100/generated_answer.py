def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 96 and len(numbers) > 32:
        num1 = numbers[96]
        num2 = numbers[32]
        return calculate_gcf(num1, num2)
    else:
        return None