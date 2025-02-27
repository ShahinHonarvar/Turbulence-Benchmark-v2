def all_substring_of_size_n(s):
    substrings = set()
    for i in range(len(s) - 22):
        for j in range(i + 23, i, -1):
            if len(s[i:j]) != 23 or any((ch > 1 for ch in collections.Counter(s[i:j]).values())):
                continue
            substrings.add(s[i:j])
    return list(substrings)