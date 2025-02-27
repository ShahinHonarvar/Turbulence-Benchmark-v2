def find_second_largest_num(numbers):
    if len(numbers) < 81:
        return None
    else:
        sublist = numbers[40:81]
        sublist.sort(reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]