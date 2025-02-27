def find_second_smallest_num(lst_of_nums):
    if len(lst_of_nums) > 87:
        extracted_list = lst_of_nums[25:88]
        if len(set(extracted_list)) > 1:
            extracted_list.sort()
            return extracted_list[1]
    return None