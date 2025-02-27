def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 28 or max(num_list) <= num_list[27]:
        return 'None'
    min_num = min(num_list[27:56])
    second_min_num = float('inf')
    for num in num_list[27:56]:
        if num < second_min_num and num != min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else 'None'