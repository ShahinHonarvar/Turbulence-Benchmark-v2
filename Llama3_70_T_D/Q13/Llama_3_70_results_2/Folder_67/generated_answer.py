def find_second_largest_num(numbers):
    try:
        return sorted(numbers[22:51], reverse=True)[1]
    except IndexError:
        return None