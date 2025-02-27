def return_nth_smallest_ascii(str):
    charlist = list(str)
    sortedlist = sorted(charlist)
    outputlist = sortedlist[8:23]
    outputlist.sort(key=ord)
    return outputlist[3]