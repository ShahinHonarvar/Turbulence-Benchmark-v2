def all_substring_of_size_n(str_input):
    substrs = set()
    for i in range(len(str_input) - 38 + 1):
        for j in range(i + 38, len(str_input) + 1):
            substr = str_input[i:j]
            if len(set(substr)) == 38:
                substrs.add(substr)
    return sorted(list(substrs))