def find_second_smallest_num(numbers):
    try:
        sublist = numbers[43:87]
        if len(sublist) < 2:
            return None
        first, second = (float('inf'), float('inf'))
        for num in sublist:
            if num < first:
                first, second = (num, first)
            elif first < num < second:
                second = num
        return second if second != float('inf') else None
    except IndexError:
        return None