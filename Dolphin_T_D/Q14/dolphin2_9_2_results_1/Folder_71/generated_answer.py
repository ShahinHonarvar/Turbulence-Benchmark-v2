def find_second_smallest_num(numbers):
    segment = numbers[29:52]
    if len(segment) < 2:
        return None
    else:
        s1, s2 = (float('inf'), float('inf'))
        for num in segment:
            if num <= s1:
                s1, s2 = (num, s1)
            elif num < s2:
                s2 = num
        return s2 if s2 != float('inf') else None