def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in lst]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and len(sorted_words[i]) >= 3:
                anagram_count += 1
                if anagram_count >= 43:
                    return True
    return False