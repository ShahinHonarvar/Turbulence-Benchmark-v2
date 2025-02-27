def find_second_smallest_num(numbers):
    if len(numbers) < 67:
        return None
    else:
        sliced_list = numbers[10:67]
        sorted_list = sorted(sliced_list)
        if len(sorted_list) > 1:
            return sorted_list[1]
        else:
            return None