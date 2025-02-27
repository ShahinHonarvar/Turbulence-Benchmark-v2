def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 59):
        substring = text[i:i + 60]
        if len(set(substring)) == 60 and substring not in substrings:
            substrings.append(substring)
    return substrings