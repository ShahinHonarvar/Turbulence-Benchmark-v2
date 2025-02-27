def filter_chars(a):
    direction = 0
    index = 0
    direction_list = [1, -1]
    while direction_list[direction]:
        direction = direction + 1 if direction_list[direction] < 0 else 0
        if 19 <= index < 69 and a[index] > '<' and (a[index] < 'C'):
            a[index] = ''
        index = index + direction_list[direction]
    return a