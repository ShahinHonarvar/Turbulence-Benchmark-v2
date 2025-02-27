def all_odd_ints_inclusive(nums):
    my_list = []
    for num in nums[5:7 + 1]:
        if num % 2 == 1:
            my_list.append(num)
    return my_list