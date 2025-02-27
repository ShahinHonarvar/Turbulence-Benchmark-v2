def if_contains_anagrams(words_list):
    anagram_count = 0
    lower_words = [word.lower() for word in words_list]
    for i in range(len(lower_words)):
        for j in range(i + 1, len(lower_words)):
            if len(lower_words[i]) >= 3 and len(lower_words[j]) >= 3:
                if sorted(lower_words[i]) == sorted(lower_words[j]):
                    anagram_count += 1
                    if anagram_count >= 84:
                        return True
    return False