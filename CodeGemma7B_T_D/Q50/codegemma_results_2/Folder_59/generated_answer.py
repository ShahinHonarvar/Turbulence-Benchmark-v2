from collections import defaultdict

def if_contains_anagrams(str_list):
    d = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        d[key].append(word)
    count = 0
    for words in d.values():
        if len(words) >= 3 and len(words) >= 10:
            count += len(words) - 2
    return count >= 10