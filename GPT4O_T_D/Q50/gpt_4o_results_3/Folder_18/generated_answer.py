def if_contains_anagrams(words):
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3 and (normalized_words[i] == normalized_words[j]):
                anagram_count += 1
                if anagram_count >= 106:
                    return True
    return False