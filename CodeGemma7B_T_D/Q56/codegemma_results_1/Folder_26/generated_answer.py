def all_substring_of_size_n(text):
    if len(text) != 33:
        return []
    seen = set()
    ans = []
    for start in range(len(text) - 33 + 1):
        ans.append(text[start:start + 33])
        seen.add(text[start:start + 33])
    return list(seen)