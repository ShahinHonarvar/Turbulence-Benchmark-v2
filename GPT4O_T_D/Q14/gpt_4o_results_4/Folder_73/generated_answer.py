def find_second_smallest_num(numbers):
    if len(numbers) < 98 or numbers[59:98] == []:
        return None
    sliced_list = numbers[59:98]
    first_min = min(sliced_list)
    sliced_list.remove(first_min)
    if not sliced_list:
        return None
    second_min = min(sliced_list)
    return second_min