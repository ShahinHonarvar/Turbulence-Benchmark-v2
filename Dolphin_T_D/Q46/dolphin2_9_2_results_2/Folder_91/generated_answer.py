def gcf_three_nums(numbers):
    a = numbers[8]
    b = numbers[9]
    c = numbers[3]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    result = gcf(a, b)
    result = gcf(result, c)
    return result