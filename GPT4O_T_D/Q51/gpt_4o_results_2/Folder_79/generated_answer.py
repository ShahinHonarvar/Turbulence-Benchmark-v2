from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = defaultdict(list)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagram_dict[sorted_word].append(word_lower)
    for group in anagram_dict.values():
        n = len(group)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 173:
                return False
    return True