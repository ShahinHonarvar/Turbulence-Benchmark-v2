def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j]:
                anagram_count += 1
                if anagram_count >= 20:
                    return True
    return False