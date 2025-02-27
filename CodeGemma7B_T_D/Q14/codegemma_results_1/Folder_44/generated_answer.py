def find_second_smallest_num(num_list):
    nums = num_list[91:100]
    if not nums:
        return 'None'
    min_num = min(nums)
    nums.remove(min_num)
    return min(nums)