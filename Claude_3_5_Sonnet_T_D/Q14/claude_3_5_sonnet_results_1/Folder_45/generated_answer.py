def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    end_index = min(200, len(numbers) - 1)
    sub_list = numbers[30:end_index + 1]
    if len(sub_list) < 2:
        return None
    smallest = min(sub_list)
    second_smallest = float('inf')
    for num in sub_list:
        if smallest < num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None