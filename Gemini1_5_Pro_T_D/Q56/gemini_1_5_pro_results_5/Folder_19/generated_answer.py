def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 17):
        substring = text[i:i + 18]
        if len(set(substring)) == 18 and substring not in substrings:
            substrings.append(substring)
    return substrings