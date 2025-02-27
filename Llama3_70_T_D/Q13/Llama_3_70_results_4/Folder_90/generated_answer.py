def find_second_largest_num(numbers):
    if len(numbers[262:747]) < 2:
        return None
    return sorted(numbers[262:747], reverse=True)[1]