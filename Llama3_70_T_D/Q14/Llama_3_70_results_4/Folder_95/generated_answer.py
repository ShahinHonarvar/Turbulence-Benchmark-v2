def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[75:86])[1]
    except IndexError:
        return None