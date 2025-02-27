from itertools import combinations

def all_substring_of_size_n(s):
    for i in range(len(s) - 145):
        temp = s[i:i + 146]
        if len(set(temp)) == 146:
            yield temp