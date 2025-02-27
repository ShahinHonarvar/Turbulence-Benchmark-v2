from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        if len(s) - i < 87:
            break
        substr = s[i:i + 87]
        if len(substr) == len(set(substr)):
            result.append(''.join(substr))
    return list(set(result))