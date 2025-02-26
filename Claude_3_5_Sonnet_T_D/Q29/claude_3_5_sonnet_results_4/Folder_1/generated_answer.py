def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 66 and isinstance(numbers[13], int) and isinstance(numbers[66], int):
        return calculate_gcf(numbers[13], numbers[66])
    else:
        return None