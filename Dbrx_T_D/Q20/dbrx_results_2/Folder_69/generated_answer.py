def find_n_th_smallest_num(numbers):
    if len(numbers) < 91 or len(numbers) > 100:
        return None
    sublist = numbers[39:92]
    sublist.sort()
    if 17 > len(sublist):
        return None
    return sublist[16]