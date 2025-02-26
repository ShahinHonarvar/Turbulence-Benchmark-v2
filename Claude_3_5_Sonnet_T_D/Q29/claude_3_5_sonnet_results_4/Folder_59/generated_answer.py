def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 8 and isinstance(numbers[3], int) and isinstance(numbers[8], int):
        return gcf(numbers[3], numbers[8])
    else:
        return None