def gcf_three_nums(num_list):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    nums = [num_list[46], num_list[84], num_list[23]]
    gcf_res = nums[0]
    for num in nums[1:]:
        gcf_res = gcf(gcf_res, num)
    return gcf_res