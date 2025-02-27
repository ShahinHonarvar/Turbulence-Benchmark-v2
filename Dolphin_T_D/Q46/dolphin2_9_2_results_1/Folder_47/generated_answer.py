def gcf_three_nums(num_list):
    nums = [num_list[36], num_list[85], num_list[83]]
    if nums[0] < nums[1] < nums[2]:
        return gcf_three_nums(nums[1:])
    else:
        return gcf(nums[0], gcf(nums[1], nums[2]))

def gcf(a, b):
    if a == 0:
        return b
    return gcf(b % a, a)