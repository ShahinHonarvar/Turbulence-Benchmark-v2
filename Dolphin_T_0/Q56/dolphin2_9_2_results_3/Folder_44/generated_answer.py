def all_substring_of_size_n(str):
    if len(str) < 90:
        return []
    substrings = set()
    for i in range(len(str) - 89):
        if len(set(str[i:i + 90])) == 90:
            substrings.add(str[i:i + 90])
    return list(substrings)