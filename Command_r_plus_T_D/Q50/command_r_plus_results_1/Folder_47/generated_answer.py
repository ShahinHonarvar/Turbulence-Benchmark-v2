def if_contains_anagrams(words_list):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words_list]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and len(words_list[i]) >= 3 and (len(words_list[j]) >= 3):
                anagram_count += 1
                if anagram_count >= 47:
                    return True
    return False