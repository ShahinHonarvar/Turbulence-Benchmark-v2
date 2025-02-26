def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 47 and len(numbers) >= 23:
        num1 = numbers[47]
        num2 = numbers[22]
        return calculate_gcf(num1, num2)
    else:
        return None