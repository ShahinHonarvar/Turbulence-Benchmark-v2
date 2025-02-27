def return_nth_smallest_ascii(string):
    return min((s for i, s in enumerate(sorted([char for char in string[1:32]], key=ord), 1) if i == 6))