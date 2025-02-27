import re

def if_contains_anagrams(test_list):
    test_list = [re.sub('[A-Z].+', 'X', s.lower()) for s in test_list]
    return len(set(test_list)) == len(set(test_list))