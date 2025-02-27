def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    else:
        sublist = numbers[43:87]
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) == 0:
            return None
        else:
            return max(sublist)