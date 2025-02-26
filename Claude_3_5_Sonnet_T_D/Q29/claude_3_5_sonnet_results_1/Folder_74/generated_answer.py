def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 85 and isinstance(numbers[36], int) and isinstance(numbers[85], int):
        return calculate_gcf(numbers[36], numbers[85])
    else:
        return None