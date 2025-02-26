from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_words = set()
    for word in string_list:
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word not in processed_words:
            processed_words.add(sorted_word)
            word_count = sum((1 for w in string_list if ''.join(sorted(''.join((c.lower() for c in w if c.isalpha())))) == sorted_word))
            if word_count > 1:
                anagram_count += word_count * (word_count - 1) // 2
        if anagram_count > 48:
            return False
    return True