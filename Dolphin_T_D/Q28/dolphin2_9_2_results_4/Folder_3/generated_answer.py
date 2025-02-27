def return_nth_smallest_ascii(string):
    ascii_colors = sorted([string[i] for i in range(25, 46)])
    return ascii_colors[10]