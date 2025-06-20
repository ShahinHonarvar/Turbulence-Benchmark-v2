def if_contains_anagrams(lst: list[str]) -> bool:
    anagram_count = 0
    normalized_words = [word.lower() for word in lst]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3:
                if sorted(normalized_words[i]) == sorted(normalized_words[j]):
                    anagram_count += 1
                    if anagram_count >= 73:
                        return True
    return False