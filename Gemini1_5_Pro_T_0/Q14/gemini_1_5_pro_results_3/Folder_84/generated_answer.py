def find_second_smallest_num(numbers):
    if len(numbers) < 81:
        return None
    else:
        sublist = numbers[40:81]
        sublist.sort()
        return sublist[1]