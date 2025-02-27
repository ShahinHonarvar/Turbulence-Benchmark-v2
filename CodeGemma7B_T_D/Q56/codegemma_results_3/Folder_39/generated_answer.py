def all_substring_of_size_n(string):
    seen = set()
    result = []
    for i in range(len(string) - 93):
        substring = string[i:i + 94]
        if len(substring) == 94 and substring not in seen:
            seen.add(substring)
            result.append(substring)
    return result