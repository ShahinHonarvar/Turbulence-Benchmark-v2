def all_substring_of_size_n(text):
    seen = set()
    for i in range(len(text) - 94):
        substring = text[i:i + 95]
        if substring not in seen:
            seen.add(substring)
    return list(seen)