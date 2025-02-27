def find_second_largest_num(num_list):
    if len(num_list) < 96:
        return None
    numbers = sorted(num_list[74:96], reverse=True)
    if len(numbers) < 2:
        return None
    return numbers[1]