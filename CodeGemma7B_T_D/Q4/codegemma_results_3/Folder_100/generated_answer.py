def all_pos_ints_exclusive(nums):
    my_new_list = []
    for number in nums:
        if number > 0 and number < 24 and (number != 22):
            my_new_list.append(number)
    if not my_new_list:
        return []
    return my_new_list