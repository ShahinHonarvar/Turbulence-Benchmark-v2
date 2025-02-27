def find_second_smallest_num(numbers):
    if len(numbers) < 10:
        return None
    else:
        temp = sorted(numbers[:10])
        if len(temp) == len(set(temp)):
            return temp[1]
        else:
            return None