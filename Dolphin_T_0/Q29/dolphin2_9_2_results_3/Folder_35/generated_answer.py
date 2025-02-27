def gcf_two_nums(numbers):

    def gcf(a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    return gcf(numbers[380], numbers[327])