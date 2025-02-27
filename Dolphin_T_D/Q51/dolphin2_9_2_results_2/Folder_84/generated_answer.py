import re

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if re.sub('\\W+', '', lst[i]).lower() == re.sub('\\W+', '', lst[j]).lower():
                    anagram_count += 1
                    if anagram_count > 16:
                        return False
    return anagram_count