def find_second_smallest_num(numbers):
    if len(numbers) < 201 or min(numbers[90:201]) == max(numbers[90:201]):
        return None
    else:
        temp = sorted(numbers[90:201])
        return temp[1]