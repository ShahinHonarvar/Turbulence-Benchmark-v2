def all_substring_of_size_n(s):
    n = 93
    substr_list = []
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if len(set(substr)) == n:
                substr_list.append(substr)
    return substr_list