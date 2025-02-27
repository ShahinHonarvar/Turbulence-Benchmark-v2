def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 60):
        substring = text[i:i + 61]
        if len(set(substring)) == 61 and substring not in substrings:
            substrings.append(substring)
    return substrings