def find_second_smallest_num(lists):
    if 8 <= len(lists) < 10:
        if len(lists) == 1:
            return None
        second_smallest = lists[8]
        for num in lists[9:]:
            if num < second_smallest:
                second_smallest = num
        if len(lists[8:]) == 1 or second_smallest == lists[8]:
            return None
        else:
            return second_smallest
    else:
        return 'Invalid list index'