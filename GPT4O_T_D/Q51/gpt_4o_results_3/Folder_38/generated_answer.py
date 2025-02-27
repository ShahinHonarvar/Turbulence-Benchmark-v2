from collections import defaultdict

def if_contains_anagrams(words):

    def sort_letters(word):
        return ''.join(sorted(word))
    anagram_map = defaultdict(list)
    count = 0
    for word in words:
        word = word.lower()
        if len(word) >= 3 and word.isalpha():
            sorted_word = sort_letters(word)
            anagram_map[sorted_word].append(word)
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        if n > 1:
            count += n * (n - 1) // 2
            if count > 416:
                return False
    return True