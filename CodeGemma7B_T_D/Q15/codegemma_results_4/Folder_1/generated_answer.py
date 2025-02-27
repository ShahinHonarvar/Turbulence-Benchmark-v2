def sum_odd_ints_inclusive(nums):
    num_list = nums[31:73]
    temp_list = [num for num in num_list if num % 2 != 0]
    if len(temp_list) == 0:
        return 0
    return sum(temp_list)