def find_second_smallest_num(nums):
    try:
        sub_nums = nums[20:201]
        second_smallest = sorted(sub_nums)[1]
        return second_smallest
    except IndexError:
        return None