def find_second_smallest_num(num_list):
    second_smallest = None
    try:
        smallest = min(num_list[17:79])
        filtered_list = [num for num in num_list[17:79] if num != smallest]
        if filtered_list:
            second_smallest = min(filtered_list)
    except (IndexError, ValueError):
        pass
    return second_smallest