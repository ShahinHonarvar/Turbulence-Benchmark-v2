from collections import Counter

def if_contains_anagrams(string_list):
    anagram_count = 0
    processed_words = set()
    for word in string_list:
        cleaned_word = ''.join(filter(str.isalpha, word.lower()))
        if len(cleaned_word) < 3:
            continue
        if cleaned_word not in processed_words:
            processed_words.add(cleaned_word)
            sorted_word = ''.join(sorted(cleaned_word))
            for other_word in string_list:
                if other_word != word:
                    cleaned_other = ''.join(filter(str.isalpha, other_word.lower()))
                    if len(cleaned_other) < 3:
                        continue
                    if ''.join(sorted(cleaned_other)) == sorted_word:
                        anagram_count += 1
                        if anagram_count > 36:
                            return False
    return True