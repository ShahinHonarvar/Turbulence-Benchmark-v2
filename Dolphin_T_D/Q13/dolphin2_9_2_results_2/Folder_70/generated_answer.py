def find_second_largest_num(numbers):
    if len(numbers) >= 33:
        sublist = numbers[28:33]
        if len(sublist) >= 2:
            max1 = max(sublist)
            sublist.remove(max1)
            if len(sublist) >= 1:
                return max(sublist)
    return None