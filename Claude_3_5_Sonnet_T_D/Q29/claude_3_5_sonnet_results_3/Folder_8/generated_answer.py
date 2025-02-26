def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 69 and len(numbers) > 41:
        num1 = numbers[69]
        num2 = numbers[41]
        return calculate_gcf(num1, num2)
    else:
        return None