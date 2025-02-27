def if_contains_anagrams(words_list):
    anagram_count = 0
    words_lower = [word.lower() for word in words_list]
    for i in range(len(words_lower)):
        for j in range(i + 1, len(words_lower)):
            if len(words_lower[i]) >= 3 and len(words_lower[j]) >= 3:
                if sorted(words_lower[i]) == sorted(words_lower[j]):
                    anagram_count += 1
                    if anagram_count >= 78:
                        return True
    return False