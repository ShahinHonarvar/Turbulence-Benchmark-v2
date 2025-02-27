def find_second_smallest_num(nums):
    sub_nums = nums[66:78]
    sub_nums.sort()
    if len(set(sub_nums)) < 2:
        return None
    for num in sub_nums:
        if sub_nums.count(num) == 2:
            sub_nums.remove(num)
            return num