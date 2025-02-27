def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if not nums[70:86]:
        return 'None'
    else:
        return nums[70:86][1]