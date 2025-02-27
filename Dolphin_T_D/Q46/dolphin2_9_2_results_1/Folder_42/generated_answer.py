def gcf_three_nums(numbers):
    nums_list = [numbers[19], numbers[69], numbers[97]]

    def greatest_common_factor(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return greatest_common_factor(nums_list[0], nums_list[1])