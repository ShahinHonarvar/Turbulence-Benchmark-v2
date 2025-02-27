def gcf_three_nums(nums):
    num_one = nums[991]
    num_two = nums[244]
    num_three = nums[974]
    gcf = gcf_three_nums_w_gvn_nums(num_one, num_two, num_three)
    return gcf

def gcf_three_nums_w_gvn_nums(num_one, num_two, num_three):
    if num_two >= num_one and num_three >= num_one or (num_two >= num_three and num_three >= num_one) or (num_one >= num_two and num_three >= num_two) or (num_one >= num_two and num_two >= num_three):
        num_one, num_two, num_three = (num_two, num_three, num_one)
    if num_one == 0:
        return num_two
    elif num_three == 0:
        return num_one
    elif num_two == 0:
        return num_three
    else:
        temp = num_one % num_two
        num_one = num_two
        num_two = temp
        temp = num_one % num_three
        num_one = num_three
        num_three = temp
        return gcf_three_nums_w_gvn_nums(num_one, num_two, num_three)