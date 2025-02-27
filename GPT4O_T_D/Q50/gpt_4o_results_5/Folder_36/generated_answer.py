from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    substrings_by_sorted = defaultdict(list)
    for string in strings:
        for i in range(len(string)):
            for j in range(i + 3, len(string) + 1):
                substring = string[i:j]
                norm = normalize(substring)
                anagram_count += len(substrings_by_sorted[norm])
                substrings_by_sorted[norm].append(substring)
                if anagram_count >= 312:
                    return True
    return False