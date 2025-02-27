def find_second_largest_num(numbers):
    if len(numbers) < 55:
        return None
    else:
        sliced_list = numbers[50:55]
        if len(set(sliced_list)) != len(sliced_list):
            return None
        else:
            sorted_list = sorted(sliced_list)
            return sorted_list[-2]