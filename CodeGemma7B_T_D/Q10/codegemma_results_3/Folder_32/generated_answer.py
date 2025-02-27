def all_odd_ints_exclusive(inlist):
    output = []
    for number in inlist[11:76]:
        if number % 2 != 0:
            output.append(number)
    return output