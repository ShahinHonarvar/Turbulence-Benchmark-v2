def all_substring_of_size_n(text, pattern_size):
    result = []
    for i in range(len(text) - pattern_size + 1):
        substring = text[i:i + pattern_size]
        if substring not in result and len(set(substring)) == pattern_size:
            result.append(substring)
    return result