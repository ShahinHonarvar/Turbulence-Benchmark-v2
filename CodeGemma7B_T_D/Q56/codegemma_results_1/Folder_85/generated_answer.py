def all_substring_of_size_n(text):
    result = []
    for left in range(len(text) - 13):
        for right in range(left + 14, len(text) + 1):
            substring = text[left:right]
            if len(set(substring)) == len(substring):
                result.append(substring)
    return result