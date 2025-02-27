def find_second_smallest_num(nums):
    try:
        sublist = nums[36:52]
        sublist.sort()
        return sublist[1]
    except IndexError:
        return None