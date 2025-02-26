def gcf_two_nums(numbers):

    def calculate_gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) < 90 or not all((isinstance(num, int) and num > 0 for num in numbers)):
        return None
    return calculate_gcf(numbers[86], numbers[89])