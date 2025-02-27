def if_contains_anagrams(word_list):
    anagram_count = 0
    processed_words = [''.join(sorted(word.lower())) for word in word_list if len(word) >= 3]
    length = len(processed_words)
    for i in range(length):
        for j in range(i + 1, length):
            if processed_words[i] == processed_words[j]:
                anagram_count += 1
                if anagram_count > 74:
                    return False
    return True