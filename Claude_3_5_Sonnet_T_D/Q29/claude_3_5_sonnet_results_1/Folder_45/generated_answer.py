def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 97 and isinstance(numbers[47], int) and isinstance(numbers[97], int):
        return calculate_gcf(numbers[47], numbers[97])
    else:
        return None