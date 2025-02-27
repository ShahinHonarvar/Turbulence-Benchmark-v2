def return_nth_smallest_ascii(string):
    if len(string) > 83:
        temp = list(string[62:84])
        temp.sort()
        return temp[8]