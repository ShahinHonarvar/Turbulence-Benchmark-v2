def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 54 and len(numbers) > 13:
        num1 = numbers[54]
        num2 = numbers[13]
        return calculate_gcf(num1, num2)
    else:
        return None