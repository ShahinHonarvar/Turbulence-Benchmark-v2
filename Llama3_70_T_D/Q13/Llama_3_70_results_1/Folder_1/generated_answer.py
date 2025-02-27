def find_second_largest_num(numbers):
    try:
        return sorted(set(numbers[31:73]), reverse=True)[1]
    except IndexError:
        return None