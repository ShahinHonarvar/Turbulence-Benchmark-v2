def gcf_two_nums(numbers_list):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(numbers_list[860], numbers_list[307])