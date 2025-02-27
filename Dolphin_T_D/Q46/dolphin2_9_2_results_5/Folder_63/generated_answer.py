def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    val38 = nums[38]
    val52 = nums[52]
    val69 = nums[69]
    result = gcf(val38, val52)
    result = gcf(result, val69)
    return result