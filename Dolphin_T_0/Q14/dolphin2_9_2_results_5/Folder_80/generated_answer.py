def find_second_smallest_num(numbers):
    if len(numbers) == 0:
        return None
    subsection = numbers[30:88]
    if len(subsection) == 0:
        return None
    x = subsection[0]
    y = None
    for i in range(1, len(subsection)):
        if subsection[i] < x:
            y = x
            x = subsection[i]
        elif y is None or subsection[i] < y:
            y = subsection[i]
    return y