def all_substring_of_size_n(text):
    substrings = set()
    for i in range(len(text) - 77):
        substring = text[i:i + 78]
        if len(set(substring)) == 78:
            substrings.add(substring)
    return list(substrings)