def find_second_largest_num(numbers):
    try:
        second_largest = sorted(numbers[29:52], reverse=True)[1]
        return second_largest
    except (IndexError, TypeError):
        return None