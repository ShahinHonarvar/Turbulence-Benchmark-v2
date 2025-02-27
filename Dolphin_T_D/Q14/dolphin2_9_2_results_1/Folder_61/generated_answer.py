def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        first, second = (float('inf'), float('inf'))
        for x in numbers:
            if x < first:
                second = first
                first = x
            elif x < second and x != first:
                second = x
        if second == float('inf'):
            return None
        else:
            return second