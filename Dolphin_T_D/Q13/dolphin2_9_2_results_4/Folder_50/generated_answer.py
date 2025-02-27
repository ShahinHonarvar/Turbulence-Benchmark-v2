def find_second_largest_num(numbers):
    temp = numbers[70:85]
    if len(temp) < 2:
        return None
    first = max(temp)
    temp.remove(first)
    if len(temp) < 2:
        return None
    return max(temp)