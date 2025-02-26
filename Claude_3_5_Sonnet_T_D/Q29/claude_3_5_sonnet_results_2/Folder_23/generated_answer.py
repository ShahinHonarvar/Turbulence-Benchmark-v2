def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 74 and isinstance(numbers[48], int) and isinstance(numbers[74], int):
        return calculate_gcf(numbers[48], numbers[74])
    else:
        return None