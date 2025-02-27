def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 55):
        substring = text[i:i + 56]
        if len(set(substring)) == 56 and substring not in substrings:
            substrings.append(substring)
    return substrings