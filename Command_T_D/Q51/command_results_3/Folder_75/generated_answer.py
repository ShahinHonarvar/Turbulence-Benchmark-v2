import re

def if_contains_anagrams(s):
    return not any((s[i] != s[j] for i in range(len(s)) for j in range(i + 1, len(s)) if re.match('[a-z]+', s[i]) == re.match('[a-z]+', s[j])))