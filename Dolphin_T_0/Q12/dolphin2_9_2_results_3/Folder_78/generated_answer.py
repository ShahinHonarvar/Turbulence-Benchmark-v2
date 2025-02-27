def find_smallest_num(list_of_numbers):
    min_num = float('inf')
    for num in list_of_numbers[36:47]:
        if num < min_num:
            min_num = num
    return min_num