def all_substring_of_size_n(string):
    if len(string) < 79:
        return []
    for i in range(len(string) - 78):
        substring = string[i:i + 79]
        if len(set(substring)) == len(substring):
            return [substring]
    return []