def all_substring_of_size_n(text):
    if len(text) < 30:
        return []
    else:
        all_substrings = set()
        for i in range(len(text) - 29):
            substring = text[i:i + 30]
            if len(substring) == len(set(substring)):
                all_substrings.add(substring)
        return list(all_substrings)