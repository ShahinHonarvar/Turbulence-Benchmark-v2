from itertools import islice

def all_substring_of_size_n(s):
    output = []
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(set(s[i:j])) == 41:
                output.append(s[i:j])
    return output