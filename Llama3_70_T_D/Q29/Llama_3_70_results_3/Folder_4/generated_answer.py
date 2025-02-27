def gcf_two_nums(nums):

    def get_gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return get_gcf(nums[76], nums[57])