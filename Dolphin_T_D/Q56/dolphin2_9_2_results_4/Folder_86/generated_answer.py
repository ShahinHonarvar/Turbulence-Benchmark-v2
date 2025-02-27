def all_substring_of_size_n(string):
    n = len(string)
    substrings = set()
    for i in range(n):
        for j in range(i + 143, n + 1):
            substrings.add(string[i:j])
    distinct_substrings = []
    for sub in substrings:
        if len(set(sub)) == len(sub):
            distinct_substrings.append(sub)
    return distinct_substrings