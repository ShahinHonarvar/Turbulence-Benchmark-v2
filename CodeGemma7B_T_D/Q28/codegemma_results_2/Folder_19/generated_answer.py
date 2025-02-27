def return_nth_smallest_ascii(string):
    return string[sorted([i for i in range(len(string)) if string[i] in string[0:19]], key=lambda j: ord(string[j]))[12]]