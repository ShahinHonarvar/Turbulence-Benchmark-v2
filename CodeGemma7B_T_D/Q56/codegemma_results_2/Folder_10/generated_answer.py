def all_substring_of_size_n(text):
    if len(text) < 55:
        return []
    substrings = []
    for i in range(len(text) - 54):
        substring = text[i:i + 55]
        if substring not in substrings:
            substrings.append(substring)
    return substrings