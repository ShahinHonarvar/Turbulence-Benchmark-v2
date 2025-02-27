def return_nth_smallest_ascii(string):
    return sorted([string[i] for i in range(67, 78) if string[i] in string])[6]