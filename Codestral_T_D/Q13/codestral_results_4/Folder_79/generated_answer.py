def find_second_largest_num(lst):
    sublist = lst[4:5]
    if len(sublist) >= 2:
        largest = second_largest = float('-inf')
        for num in sublist:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest and num < largest:
                second_largest = num
        return second_largest if second_largest != float('-inf') else None
    else:
        return None