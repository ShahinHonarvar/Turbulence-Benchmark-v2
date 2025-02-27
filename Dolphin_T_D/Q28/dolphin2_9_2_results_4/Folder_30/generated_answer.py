def return_nth_smallest_ascii(string):
    members = []
    for i in range(50, 77):
        if string[i].isalpha():
            members.append(ord(string[i]))
    n = len(members)
    if n < 11:
        return None
    else:
        return chr(sorted(members)[10])