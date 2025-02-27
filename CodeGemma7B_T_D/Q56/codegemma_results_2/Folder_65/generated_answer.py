def all_substring_of_size_n(text):
    results = set()
    if len(text) < 81:
        return list(results)
    for start in range(len(text) - 81 + 1):
        substring = text[start:start + 81]
        if len(set(substring)) == 81:
            results.add(substring)
    return list(results)