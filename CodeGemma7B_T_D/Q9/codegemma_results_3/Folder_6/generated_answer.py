def all_odd_ints_inclusive(nums):
    my_list = nums[10:67]
    res = [num for num in my_list if num % 2 != 0]
    return res or []