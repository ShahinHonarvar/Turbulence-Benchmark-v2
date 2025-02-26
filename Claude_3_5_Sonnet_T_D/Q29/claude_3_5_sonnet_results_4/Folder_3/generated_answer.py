def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 47 and len(numbers) >= 11:
        return calculate_gcf(numbers[47], numbers[10])
    else:
        return None