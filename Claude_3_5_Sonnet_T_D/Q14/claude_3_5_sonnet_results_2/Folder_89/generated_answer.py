def find_second_smallest_num(numbers):
    if len(numbers) < 64 or len(numbers[62:64]) < 2:
        return None
    sublist = numbers[62:64]
    if sublist[0] != sublist[1]:
        return max(sublist)
    else:
        return None