def find_second_largest_num(numbers):
    sub_list = numbers[12:93]
    unique_nums = list(set(sub_list))
    if len(unique_nums) < 2:
        return None
    else:
        unique_nums.sort(reverse=True)
        return unique_nums[1]