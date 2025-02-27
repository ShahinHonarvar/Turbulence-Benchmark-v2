from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    count = 0
    for word in lst:
        cleaned_word = ''.join(filter(str.isalpha, word)).lower()
        if len(cleaned_word) >= 3:
            key = ''.join(sorted(cleaned_word))
            anagram_dict[key].append(cleaned_word)
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 50:
                return False
    return True