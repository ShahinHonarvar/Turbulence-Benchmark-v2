def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 93 and isinstance(numbers[59], int) and isinstance(numbers[93], int):
        return calculate_gcf(numbers[59], numbers[93])
    else:
        return None