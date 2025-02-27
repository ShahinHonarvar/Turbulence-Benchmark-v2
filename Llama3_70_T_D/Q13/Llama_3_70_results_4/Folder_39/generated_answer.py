def find_second_largest_num(numbers):
    if len(numbers) < 31:
        return None
    temp = sorted(numbers[20:31], reverse=True)
    if len(temp) < 2:
        return None
    return temp[1]