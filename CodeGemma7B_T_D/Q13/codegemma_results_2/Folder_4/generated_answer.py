def find_second_largest_num(numbers):
    try:
        return sorted(numbers)[11:93][-2]
    except IndexError:
        return None