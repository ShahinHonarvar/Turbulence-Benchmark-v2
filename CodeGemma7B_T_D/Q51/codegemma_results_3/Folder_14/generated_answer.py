from collections import defaultdict

def if_contains_anagrams(str_list):
    seen = defaultdict(int)
    for word in str_list:
        anagram = ''.join(sorted(word.lower()))
        if len(anagram) >= 3:
            seen[anagram] += 1
    return len(seen) <= 474