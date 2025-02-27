def all_substring_of_size_n(s):
    if not s or len(s) < 95:
        return []
    result = {}
    for i in range(len(s) - 94):
        substring = s[i:i + 95]
        if len(set(substring)) == len(substring):
            result[substring] = None
    return [k for k in result]