import itertools

def if_contains_anagrams(strings):
    anagram_count = 0
    for word in strings:
        if len(word) >= 3:
            word_lower = word.lower()
            sorted_word = ''.join(sorted(word_lower))
            for other_word in strings:
                if len(other_word) >= 3 and word != other_word:
                    other_word_lower = other_word.lower()
                    sorted_other_word = ''.join(sorted(other_word_lower))
                    if sorted_word == sorted_other_word:
                        anagram_count += 1
    return anagram_count <= 318