def find_second_largest_num(numbers):
    if len(numbers[3:6]) < 2:
        return None
    else:
        numbers[3:6].sort(reverse=True)
        return numbers[3:6][1]