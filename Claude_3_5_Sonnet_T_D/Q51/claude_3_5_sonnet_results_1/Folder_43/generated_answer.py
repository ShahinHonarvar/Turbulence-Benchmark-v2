from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed = set()
    for i, word in enumerate(string_list):
        if word in processed or len(word) < 3:
            continue
        cleaned_word = ''.join((char.lower() for char in word if char.isalpha()))
        if len(cleaned_word) < 3:
            continue
        word_counter = Counter(cleaned_word)
        for j in range(i + 1, len(string_list)):
            compare_word = string_list[j]
            if compare_word in processed or len(compare_word) < 3:
                continue
            cleaned_compare = ''.join((char.lower() for char in compare_word if char.isalpha()))
            if len(cleaned_compare) < 3:
                continue
            if word_counter == Counter(cleaned_compare):
                anagram_count += 1
                processed.add(word)
                processed.add(compare_word)
                break
        if anagram_count > 3:
            return False
    return True