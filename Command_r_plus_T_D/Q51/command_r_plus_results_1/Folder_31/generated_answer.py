def normalize_string(s):
    return ''.join((c for c in s.lower() if c.isalpha()))

def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_string(word)
        if len(normalized_word) < 3:
            continue
        sorted_word = ''.join(sorted(normalized_word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
        if len(anagram_dict[sorted_word]) > 1:
            anagram_count += 1
    return anagram_count <= 65