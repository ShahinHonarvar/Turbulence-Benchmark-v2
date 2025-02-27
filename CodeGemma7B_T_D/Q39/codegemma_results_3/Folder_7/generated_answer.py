def return_n_greatest_chars(string):
    occurrences = {}
    for char in string:
        occurrences[char] = occurrences.get(char, 0) + 1
    sorted_chars = sorted(occurrences.keys(), key=ord)
    return sorted_chars[-49:]