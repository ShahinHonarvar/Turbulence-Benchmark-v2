def all_substring_of_size_n(string):
    results = set()
    for i in range(len(string) - 45):
        substring = string[i:i + 46]
        results.add(substring)
    return list(results)