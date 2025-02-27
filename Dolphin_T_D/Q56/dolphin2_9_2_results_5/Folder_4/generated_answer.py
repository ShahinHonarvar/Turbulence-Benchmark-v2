def all_substring_of_size_n(String):
    Substrings = []
    for i in range(len(String) - 40):
        Substring = String[i:i + 41]
        if len(set(Substring)) == 41:
            Substrings.append(Substring)
    return Substrings