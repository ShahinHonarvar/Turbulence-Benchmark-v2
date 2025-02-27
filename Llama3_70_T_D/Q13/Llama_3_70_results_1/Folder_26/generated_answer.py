def find_second_largest_num(lst):
    if len(lst) < 100:
        return None
    else:
        second_largest = None
        largest = float('-inf')
        for i in range(62, 100):
            if lst[i] > largest:
                second_largest = largest
                largest = lst[i]
            elif lst[i] < largest and (second_largest is None or lst[i] > second_largest):
                second_largest = lst[i]
        return second_largest