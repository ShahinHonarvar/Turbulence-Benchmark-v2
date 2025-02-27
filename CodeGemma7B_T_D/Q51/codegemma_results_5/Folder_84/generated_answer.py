from collections import Counter

def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = [s for s in str_list if len(s) >= 3]
    anagrams = set()
    for s in str_list:
        counter = Counter(s)
        sorted_str = ''.join(sorted(counter.elements()))
        anagrams.add(sorted_str)
    return len(anagrams) <= 16