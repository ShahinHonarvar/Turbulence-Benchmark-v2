def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return 'None'
    else:
        sliced_list = numbers[22:51]
        if len(set(sliced_list)) < 2:
            return 'None'
        else:
            sorted_list = sorted(sliced_list)
            return sorted_list[-2]