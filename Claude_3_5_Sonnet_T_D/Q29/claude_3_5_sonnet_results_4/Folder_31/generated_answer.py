def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 95 and isinstance(numbers[87], int) and isinstance(numbers[95], int):
        return gcf(numbers[87], numbers[95])
    else:
        return None