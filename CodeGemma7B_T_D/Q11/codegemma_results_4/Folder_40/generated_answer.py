def find_largest_num(nums):
    largest_num = nums[0]
    for num in nums[1:3]:
        if num > largest_num:
            largest_num = num
    print('The largest number is:', largest_num)