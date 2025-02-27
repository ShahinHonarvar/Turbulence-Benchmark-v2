def return_nth_smallest_ascii(str0):
    lst = [ord(i) for i in str0]
    lst.sort()
    print(chr(lst[11]))