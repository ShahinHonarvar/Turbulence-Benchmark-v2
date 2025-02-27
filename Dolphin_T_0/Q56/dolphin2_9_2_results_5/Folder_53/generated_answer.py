def all_substring_of_size_n(s):
    subs = [s[i:i + 25] for i in range(len(s) - 24)]
    return [sub for sub in set(subs) if len(set(sub)) == len(sub)]