def all_substring_of_size_n(s):
    return list({s[i:i + 127] for i in range(len(s)) if len(s[i:i + 127]) == 127 and len(set(s[i:i + 127])) == 127})