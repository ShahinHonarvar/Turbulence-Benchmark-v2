def all_substring_of_size_n(str1):
    str1 = str1.lower()
    subs = set()
    for i in range(len(str1)):
        for j in range(i + 19, len(str1) + 1):
            subs.add(str1[i:j])
    return list(subs)