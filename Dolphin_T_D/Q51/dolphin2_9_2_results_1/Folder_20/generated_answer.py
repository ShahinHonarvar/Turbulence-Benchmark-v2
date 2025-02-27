from collections import Counter

def if_contains_anagrams(lst):
    num_anagrams = 0
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            word = word.lower()
            char_count = Counter(word)
            for other_word in lst:
                if word != other_word and len(other_word) >= 3 and other_word.isalpha():
                    other_word = other_word.lower()
                    other_char_count = Counter(other_word)
                    if char_count == other_char_count:
                        num_anagrams += 1
    return num_anagrams <= 131