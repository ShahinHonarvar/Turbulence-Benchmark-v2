def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 5:
        return None
    return calculate_gcf(numbers[4], numbers[0])