def find_second_smallest_num(numbers):
    if len(numbers) >= 66:
        sublist = numbers[64:67]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
        else:
            return 'None'
    else:
        return 'None'