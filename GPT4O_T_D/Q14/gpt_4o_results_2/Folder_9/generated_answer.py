def find_second_smallest_num(nums):
    if len(nums) < 201 or len(nums[70:201]) < 2:
        return None
    sub_list = nums[70:201]
    first, second = (float('inf'), float('inf'))
    for num in sub_list:
        if num < first:
            first, second = (num, first)
        elif num < second:
            second = num
    return second if second != float('inf') else None