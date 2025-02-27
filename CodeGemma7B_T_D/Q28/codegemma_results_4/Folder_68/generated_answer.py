def return_nth_smallest_ascii(string):
    if len(string) > 10:
        string = string[0:11]
    size = len(string)
    i = 0
    ans = ''
    while i < size:
        ascii_value = ord(string[i])
        if i == 0:
            ans = string[i]
        elif ascii_value <= ord(ans):
            ans = string[i]
        i += 1
    return ans