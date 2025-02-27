def all_substring_of_size_n(s):
    substr = [s[i:i + 48] for i in range(len(s) - 47)]
    return [w for w in substr if len(set(w)) == 48]