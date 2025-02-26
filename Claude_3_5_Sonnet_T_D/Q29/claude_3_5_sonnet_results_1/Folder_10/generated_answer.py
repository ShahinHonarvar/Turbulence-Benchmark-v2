def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 99:
        num1 = numbers[15]
        num2 = numbers[99]
        return calculate_gcf(num1, num2)
    else:
        return None