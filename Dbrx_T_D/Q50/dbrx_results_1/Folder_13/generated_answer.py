import re
from collections import Counter

def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(re.findall('\\\\w', string.lower())))
            anagrams.append(Counter(sorted_string))
    pairs = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j] and anagrams[i] not in [anagrams[k] for k in range(i)]:
                pairs += 1
    return True if pairs >= 144 else False