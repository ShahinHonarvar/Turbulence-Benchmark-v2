def gcf_two_nums(list_of_nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(list_of_nums[21], list_of_nums[17])