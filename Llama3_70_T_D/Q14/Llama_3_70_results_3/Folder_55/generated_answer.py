def find_second_smallest_num(num_list):
    if len(num_list) > 10:
        nums = num_list[10:]
        unique_nums = []
        for num in nums:
            if num not in unique_nums:
                unique_nums.append(num)
        unique_nums.sort()
        if len(unique_nums) > 1:
            return unique_nums[1]
    return None