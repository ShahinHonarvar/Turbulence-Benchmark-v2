def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text.lower() if e.isalpha()))
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        sorted_word = ''.join(sorted(normalized_word))
        if sorted_word in anagram_dict:
            anagram_count += 1
            if anagram_count > 289:
                return False
        else:
            anagram_dict[sorted_word] = normalized_word
    return True