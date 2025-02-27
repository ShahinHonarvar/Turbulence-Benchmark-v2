def find_second_largest_num(numbers):
    if len(numbers) < 101:
        return None
    else:
        temp = sorted(numbers[10:101], reverse=True)
        if len(temp) < 2:
            return None
        else:
            return temp[1]