def return_nth_smallest_ascii(str):
    temp = []
    for i in str[15:22]:
        temp.append(ord(i))
    temp.sort()
    return chr(temp[5])