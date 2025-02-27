def all_substring_of_size_n(str1):
    return [str1[x:x + 56] for x in range(len(str1) - 55) if len(set(str1[x:x + 56])) == 56]