def if_contains_anagrams(strings):

    def is_anagram(word1, word2):
        return sorted(word1) == sorted(word2)
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    count = 0
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if len(normalized_strings[i]) >= 3 and len(normalized_strings[j]) >= 3:
                if is_anagram(normalized_strings[i], normalized_strings[j]):
                    count += 1
                    if count > 43:
                        return False
    return True