def all_pos_ints_exclusive(numbers_list):
    exclusive_range = numbers_list[111:473]
    positive_numbers = [num for num in exclusive_range if num > 0]
    return positive_numbers