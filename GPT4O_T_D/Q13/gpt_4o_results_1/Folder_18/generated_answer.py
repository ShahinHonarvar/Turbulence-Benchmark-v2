def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    sliced_list = numbers[35:50]
    unique_sliced_list = list(set(sliced_list))
    if len(unique_sliced_list) < 2:
        return None
    unique_sliced_list.sort(reverse=True)
    return unique_sliced_list[1]