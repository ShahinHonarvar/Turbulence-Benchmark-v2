def all_substring_of_size_n(string):
    if len(string) < 96:
        return []
    result = set()
    for i in range(len(string) - 95):
        subs = string[i:i + 96]
        if len(set(subs)) == len(subs):
            result.add(subs)
    return list(result)