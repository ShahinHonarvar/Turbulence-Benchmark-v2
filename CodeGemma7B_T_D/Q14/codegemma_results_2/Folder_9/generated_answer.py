def find_second_smallest_num(lst):
    second_smallest = float('inf')
    for num in lst[70:201]:
        if num < second_smallest and num != min(lst[70:201]):
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None