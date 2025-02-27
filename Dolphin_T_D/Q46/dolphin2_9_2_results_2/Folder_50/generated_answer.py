def gcf_three_nums(nums):
    gcf = nums[20]
    for i in range(20, 75):
        if i not in {20, 35, 74}:
            if gcf % nums[i] == 0:
                gcf = gcf // nums[i]
            else:
                gcf = gcf * nums[i]
    return gcf