def find_second_smallest_num(numbers):
    if len(numbers) < 610:
        return None
    else:
        sliced_list = numbers[608:610]
        if len(set(sliced_list)) == 1:
            return None
        else:
            return sorted(sliced_list)[1]