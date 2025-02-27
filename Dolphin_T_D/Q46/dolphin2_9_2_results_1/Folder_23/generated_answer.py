def gcf_three_nums(numbers):
    numbers = [numbers[31], numbers[25], numbers[80]]

    def gcf(a, b):
        if a == 0 or b == 0:
            return 0
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = gcf(result, numbers[i])
    return result