import re

def sorted_string(s):
    return ''.join(sorted(re.findall('\\b\\w{3,}\\b', s.lower())))

def count_anagrams(strings):
    return len(list(filter(lambda x: x[1] > 1, dict(list(Counter(map(sorted_string, strings)).items()).values()))))

def if_contains_anagrams(strings):
    return count_anagrams(strings) <= 40