from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    strings = [s.lower() for s in strings if len(s) >= 3]
    anagram_count = 0
    seen = defaultdict(list)
    for i, word in enumerate(strings):
        sort_word = ''.join(sorted(word))
        for j in seen[sort_word]:
            if is_anagram(strings[j], word):
                anagram_count += 1
                if anagram_count > 116:
                    return False
        seen[sort_word].append(i)
    return anagram_count <= 116