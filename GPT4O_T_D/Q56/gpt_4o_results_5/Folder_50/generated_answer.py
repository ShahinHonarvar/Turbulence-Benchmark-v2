def all_substring_of_size_n(s):

    def has_unique_chars(subs):
        return len(set(subs)) == len(subs)
    result = []
    for i in range(len(s) - 10):
        substr = s[i:i + 11]
        if has_unique_chars(substr):
            result.append(substr)
    return result