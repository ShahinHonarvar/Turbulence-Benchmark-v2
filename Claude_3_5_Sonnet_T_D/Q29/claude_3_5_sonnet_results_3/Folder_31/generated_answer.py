def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 95 and isinstance(numbers[87], int) and isinstance(numbers[95], int) and (numbers[87] > 0) and (numbers[95] > 0):
        return calculate_gcf(numbers[87], numbers[95])
    else:
        return None