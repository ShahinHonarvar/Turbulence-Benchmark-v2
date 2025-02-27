def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 89):
        substring = text[i:i + 90]
        if len(set(substring)) == 90:
            substrings.add(substring)
    return list(substrings)