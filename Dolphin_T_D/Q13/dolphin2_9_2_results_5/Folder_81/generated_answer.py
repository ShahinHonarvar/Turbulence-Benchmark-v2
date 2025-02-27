def find_second_largest_num(lst):
    if 10 <= len(lst) <= 100:
        lst = lst[10:101]
        if len(lst) > 1:
            largest = second_largest = lst[0]
            for num in lst[1:]:
                if num > largest:
                    second_largest = largest
                    largest = num
                elif second_largest < num < largest:
                    second_largest = num
            return second_largest
    return None