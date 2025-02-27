def find_second_largest_num(num_list):
    if len(num_list) < 2 or len(num_list) - 1 < 56 or 57 < len(num_list) - 1:
        return None
    else:
        extracted_nums = num_list[56:58]
        sorted_nums = sorted(extracted_nums)
        if len(sorted_nums) == 1:
            return sorted_nums[0]
        else:
            return sorted_nums[0]