def all_substring_of_size_n(s):

    def has_no_duplicates(sub):
        return len(set(sub)) == len(sub)
    return list(set([s[i:i + 110] for i in range(len(s) - 109) if has_no_duplicates(s[i:i + 110])]))