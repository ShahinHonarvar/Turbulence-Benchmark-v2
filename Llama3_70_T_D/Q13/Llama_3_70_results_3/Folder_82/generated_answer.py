def find_second_largest_num(numbers):
    if len(numbers) < 201:
        return None
    temp = sorted(numbers[20:201], reverse=True)
    if len(temp) < 2:
        return None
    return temp[1]