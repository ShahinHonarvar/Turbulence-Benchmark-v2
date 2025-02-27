def find_second_smallest_num(my_list):
    if len(my_list) < 96:
        return None
    sublist = my_list[74:96]
    unique_numbers = list(set(sublist))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]