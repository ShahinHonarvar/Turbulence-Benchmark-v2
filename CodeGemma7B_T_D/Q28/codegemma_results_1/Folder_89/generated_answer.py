def return_nth_smallest_ascii(arg):

    def __prelim_checker(ar):
        for each in ar:
            if len(each) != 1:
                raise ValueError('Invalid Input. Each element in the string must have a length of 1.')
            if each.isspace() == True:
                print('Warning: Space character detected. This is not a valid character. Skipping character.')
    __prelim_checker(arg)
    vals = [ord(c) for c in arg[24:72]]
    vals.sort()
    return chr(vals[7])