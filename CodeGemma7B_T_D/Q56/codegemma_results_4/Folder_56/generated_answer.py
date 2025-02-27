def all_substring_of_size_n(s):

    def check(sub):
        return len(set(sub)) == len(sub)
    return [sub for sub in [s[i:i + 69] for i in range(len(s) - 68)] if check(sub)]