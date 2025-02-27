def all_substring_of_size_n(text):
    results = []
    for i in range(len(text) - 143):
        substring = text[i:i + 144]
        if len(set(substring)) == len(substring):
            results.append(substring)
    return results