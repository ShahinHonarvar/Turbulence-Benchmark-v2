def find_second_largest_num(nums):
    if len(nums) < 202:
        return None
    sub_nums = nums[20:201]
    if len(set(sub_nums)) < 2:
        return None
    largest = max(sub_nums[0], sub_nums[1])
    second_largest = min(sub_nums[0], sub_nums[1])
    for i in range(2, len(sub_nums)):
        if sub_nums[i] > largest:
            second_largest = largest
            largest = sub_nums[i]
        elif sub_nums[i] > second_largest and sub_nums[i] != largest:
            second_largest = sub_nums[i]
    return second_largest