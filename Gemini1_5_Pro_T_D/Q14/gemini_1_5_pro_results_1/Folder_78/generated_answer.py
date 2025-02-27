def find_second_smallest_num(numbers):
    if len(numbers) < 79 or min(numbers[17:79]) == max(numbers[17:79]):
        return None
    else:
        temp = sorted(numbers[17:79])
        return temp[1]