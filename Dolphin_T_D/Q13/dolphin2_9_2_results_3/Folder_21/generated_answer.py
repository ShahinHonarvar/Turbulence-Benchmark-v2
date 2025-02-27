def find_second_largest_num(lst):
    if lst:
        if len(lst) < 976:
            return None
        sublist = lst[639:976]
        largest = second_largest = float('-inf')
        for number in sublist:
            if number > largest:
                second_largest = largest
                largest = number
            elif number > second_largest and number < largest:
                second_largest = number
        if second_largest != float('-inf'):
            return second_largest
    return None