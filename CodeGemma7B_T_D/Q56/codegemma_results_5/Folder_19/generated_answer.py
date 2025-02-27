def all_substring_of_size_n(text):
    if len(text) < 18:
        return []
    all_substring = set()
    for i in range(0, len(text)):
        for j in range(i + 18, len(text) + 1):
            current_substring = text[i:j]
            if len(current_substring) == 18 and len(set(current_substring)) == 18:
                all_substring.add(current_substring)
    return list(all_substring)