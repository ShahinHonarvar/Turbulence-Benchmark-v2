def all_substring_of_size_n(s):
    list_of_substring = []
    for i in range(len(s)):
        for j in range(i + substring_size):
            if len(set(s[i:j])) == substring_size and substring_size + i <= j:
                list_of_substring.append(s[i:j])
    return list_of_substring