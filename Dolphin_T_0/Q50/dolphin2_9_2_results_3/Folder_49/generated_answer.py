from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                count = 0
                s1 = ''.join(sorted(strings[i].lower()))
                s2 = ''.join(sorted(strings[j].lower()))
                if s1 == s2 and strings[i] != strings[j]:
                    count += 1
                    anagram_count += count
    return anagram_count >= 59