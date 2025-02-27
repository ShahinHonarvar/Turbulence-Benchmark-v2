def all_substring_of_size_n(text):
    if len(text) < 85:
        return []

    def is_valid(substring):
        return len(set(substring)) == len(substring)
    result = []
    for i in range(len(text) - 84 + 1):
        substring = text[i:i + 85]
        if is_valid(substring):
            result.append(substring)
    return result