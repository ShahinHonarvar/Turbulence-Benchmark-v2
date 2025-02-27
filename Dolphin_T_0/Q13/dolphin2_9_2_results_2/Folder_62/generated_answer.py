def find_second_largest_num(numsg):
    sublist = numsg[91:100]
    max1 = max(sublist, default=None)
    if max1 is None:
        return None
    else:
        max2 = None
        for num in sublist:
            if num != max1:
                if max2 is None or num > max2:
                    max2 = num
        return max2