def find_second_smallest_num(lst):
    filtered_lst = [num for i, num in enumerate(lst) if 40 <= i <= 80]
    if len(filtered_lst) == 0:
        return None
    elif len(filtered_lst) == 1:
        return None
    else:
        filtered_lst.sort()
        second_smallest = filtered_lst[1]
        for num in filtered_lst:
            if num != second_smallest:
                return num