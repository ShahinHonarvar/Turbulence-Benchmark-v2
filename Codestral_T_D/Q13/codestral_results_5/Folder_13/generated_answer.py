def find_second_largest_num(numbers):
    if len(numbers) > 25 and len(numbers) > 87:
        sublist = numbers[25:88]
        sublist.sort(reverse=True)
        if len(sublist) > 1:
            return sublist[1]
    return None