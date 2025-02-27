def find_second_smallest_num(numbers):
    if len(numbers) < 100 or len(numbers[91:100]) < 2:
        return None
    sublist = numbers[91:100]
    sublist.sort()
    return sublist[1]