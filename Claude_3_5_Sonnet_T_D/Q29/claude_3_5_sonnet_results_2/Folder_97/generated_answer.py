def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 312:
        num1 = numbers[180]
        num2 = numbers[312]
        return calculate_gcf(num1, num2)
    else:
        return None