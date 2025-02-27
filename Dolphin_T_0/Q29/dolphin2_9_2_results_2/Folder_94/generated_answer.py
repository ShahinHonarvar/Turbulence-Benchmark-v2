def gcf_two_nums(numbers):

    def gcf_two_numbers(a, b):
        if b == 0:
            return a
        else:
            return gcf_two_numbers(b, a % b)
    return gcf_two_numbers(numbers[91], numbers[45])