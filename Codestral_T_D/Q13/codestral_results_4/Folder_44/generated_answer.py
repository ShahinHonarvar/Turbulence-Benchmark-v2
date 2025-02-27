def find_second_largest_num(numbers):
    sub_list = numbers[13:69]
    sub_list.sort(reverse=True)
    unique_nums = []
    for num in sub_list:
        if num not in unique_nums:
            unique_nums.append(num)
        if len(unique_nums) == 2:
            return unique_nums[1]
    return None