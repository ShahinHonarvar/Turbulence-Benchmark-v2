def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 37 and isinstance(numbers[18], int) and isinstance(numbers[37], int) and (numbers[18] > 0) and (numbers[37] > 0):
        return calculate_gcf(numbers[18], numbers[37])
    else:
        return None