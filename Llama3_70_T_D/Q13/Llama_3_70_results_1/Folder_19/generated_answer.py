def find_second_largest_num(numbers):
    try:
        temp = sorted(numbers[3:6], reverse=True)
        if len(temp) < 2:
            return None
        return temp[1]
    except IndexError:
        return None