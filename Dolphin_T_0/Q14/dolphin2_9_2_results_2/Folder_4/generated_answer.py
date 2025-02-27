def find_second_smallest_num(lst):
    if not lst[70:85]:
        return 'None'
    else:
        min_1 = min(lst[70:85])
        min_2 = min((val for val in lst[70:85] if val != min_1))
        return min_2