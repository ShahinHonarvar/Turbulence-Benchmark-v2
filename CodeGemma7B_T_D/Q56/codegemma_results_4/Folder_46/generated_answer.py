from collections import defaultdict

def all_substring_of_size_n(s):
    res = []
    for i in range(len(s) - 86):
        temp = s[i:i + 87]
        if len(set(temp)) == 87:
            res.append(temp)
    return res