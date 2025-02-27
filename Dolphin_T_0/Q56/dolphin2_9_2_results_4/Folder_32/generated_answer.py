def all_substring_of_size_n(mystring):
    length = len(mystring)
    if length < 71:
        return []
    mylist = []
    for i in range(0, length - 70):
        mysubstring = mystring[i:i + 71]
        if len(set(mysubstring)) == 71:
            mylist.append(mysubstring)
    return mylist