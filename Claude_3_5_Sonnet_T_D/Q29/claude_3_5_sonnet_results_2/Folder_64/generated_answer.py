def gcf_two_nums(numbers):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(numbers) > 9 and isinstance(numbers[6], int) and isinstance(numbers[9], int):
        return gcf(numbers[6], numbers[9])
    else:
        return None