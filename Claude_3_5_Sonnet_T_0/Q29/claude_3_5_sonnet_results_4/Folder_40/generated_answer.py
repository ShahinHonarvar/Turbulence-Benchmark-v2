def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 9 and isinstance(numbers[7], int) and isinstance(numbers[9], int):
        return calculate_gcf(numbers[7], numbers[9])
    else:
        return None