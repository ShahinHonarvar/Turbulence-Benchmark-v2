def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 45):
        substring = text[i:i + 46]
        if len(set(substring)) == 46 and substring not in substrings:
            substrings.append(substring)
    return substrings