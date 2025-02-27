from collections import Counter

def all_substring_of_size_n(str1):
    res = []
    for i in range(len(str1)):
        for j in range(i + 1, len(str1)):
            substr = str1[i:j + 1]
            if len(substr) == 97 and len(Counter(substr)) == len(substr):
                res.append(substr)
    return res