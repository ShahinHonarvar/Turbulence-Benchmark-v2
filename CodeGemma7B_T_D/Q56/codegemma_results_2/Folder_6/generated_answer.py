def all_substring_of_size_n(text):
    results = set()
    for i in range(len(text) - 22):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j + 1]
            if len(set(substring)) == len(substring):
                results.add(substring)
    return list(results)