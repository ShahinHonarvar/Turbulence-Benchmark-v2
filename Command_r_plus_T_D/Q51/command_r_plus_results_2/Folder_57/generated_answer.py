def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text if e.isalpha())).lower()
    anagram_count = 0
    anagram_set = set()
    for word in lst:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        sorted_word = ''.join(sorted(normalized_word))
        if sorted_word in anagram_set:
            anagram_count += 1
        else:
            anagram_set.add(sorted_word)
    return anagram_count <= 74