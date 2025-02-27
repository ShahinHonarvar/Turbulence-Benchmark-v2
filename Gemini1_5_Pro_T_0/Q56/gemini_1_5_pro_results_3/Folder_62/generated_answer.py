def all_substring_of_size_n(text):
    substrings = []
    for i in range(len(text) - 31):
        substring = text[i:i + 32]
        if len(set(substring)) == 32 and substring not in substrings:
            substrings.append(substring)
    return substrings