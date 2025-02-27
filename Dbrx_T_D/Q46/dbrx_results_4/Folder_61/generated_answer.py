def gcf_three_nums(numbers):

    def greatest_common_factor(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    nums_to_consider = [numbers[1], numbers[2], numbers[7]]
    return greatest_common_factor(nums_to_consider[0], nums_to_consider[1]) if len(nums_to_consider) == 3 else None