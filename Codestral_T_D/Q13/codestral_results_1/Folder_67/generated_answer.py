def find_second_largest_num(nums):
    sublist = nums[22:51]
    sublist.sort(reverse=True)
    second_largest = None
    for num in sublist:
        if num != sublist[0]:
            second_largest = num
            break
    return second_largest