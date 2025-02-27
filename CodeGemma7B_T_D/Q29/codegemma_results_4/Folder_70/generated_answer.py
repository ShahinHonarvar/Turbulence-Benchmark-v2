def gcf_two_nums(nums):
    num_300 = nums[300]
    num_616 = nums[616]
    cf = min([num_300, num_616])
    while cf > 0:
        if num_300 % cf == 0 and num_616 % cf == 0:
            return cf
        cf -= 1