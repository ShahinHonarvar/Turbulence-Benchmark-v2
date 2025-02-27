from collections import defaultdict

def all_substring_of_size_n(s):
    result = []
    if len(s) < 26:
        return result
    substr_map = defaultdict(lambda: -1)
    for i in range(len(s) - 25):
        current_substr = s[i:i + 26]
        if len(current_substr) != 26:
            continue
        unique_chars = len(set(current_substr))
        if unique_chars == len(current_substr):
            if substr_map[current_substr] == -1:
                result.append(current_substr)
                substr_map[current_substr] = i
    return result