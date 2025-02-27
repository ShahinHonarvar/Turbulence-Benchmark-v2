def gcf_two_nums(nums):

    def gcf(x, y):
        for i in range(min(x, y), 0, -1):
            if x % i == 0 and y % i == 0:
                return i
    return gcf(nums[180], nums[312])