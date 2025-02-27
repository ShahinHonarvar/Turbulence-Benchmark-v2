def all_substring_of_size_n(string):
    n = len(string)
    substrings = []
    counter = 0
    for i in range(n):
        for j in range(i + 5, n):
            sub = string[i:j]
            if len(set(sub)) == len(sub) and len(sub) == 105:
                substrings.append(sub)
    distinct_substrings = list(set(substrings))
    return distinct_substrings