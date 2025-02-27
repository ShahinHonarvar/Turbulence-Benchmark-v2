def find_second_smallest_num(numbers):
    if len(numbers) < 69:
        return None
    else:
        sliced_list = numbers[42:69]
        if len(set(sliced_list)) == len(sliced_list):
            sorted_list = sorted(sliced_list)
            return sorted_list[1]
        else:
            return None