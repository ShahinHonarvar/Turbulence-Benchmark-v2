def find_second_largest_num(numbers):
    if len(numbers) < 5:
        return None
    else:
        temp = sorted(numbers[4:5])
        if len(temp) >= 2:
            return temp[1]
        else:
            return None