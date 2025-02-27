def find_second_smallest_num(numbers):
    sublist = numbers[31:35]
    if len(sublist) < 2:
        return None
    else:
        min1, min2 = (float('inf'), float('inf'))
        for x in sublist:
            if x <= min1:
                min1, min2 = (x, min1)
            elif x < min2:
                min2 = x
        return min2 if min2 != float('inf') else None