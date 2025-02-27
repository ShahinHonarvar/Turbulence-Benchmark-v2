def all_substring_of_size_n(word):
    if len(word) < 35:
        return []
    result = set()
    for i in range(len(word) - 34):
        substring = word[i:i + 35]
        if len(substring) == 35 and len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)