import string

def if_contains_anagrams(words):
    anagram_count = 0
    english_letters = set(string.ascii_lowercase)
    for word in words:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        if sorted_word.count(''.join(set(sorted_word) & english_letters)) >= 2:
            anagram_count += 1
            if anagram_count > 57:
                return False
    return True