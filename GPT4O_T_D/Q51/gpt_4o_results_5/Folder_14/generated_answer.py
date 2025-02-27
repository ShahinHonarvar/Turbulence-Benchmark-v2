def if_contains_anagrams(lst):
    anagram_count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    seen = {}
    for word in normalized_words:
        if word in seen:
            anagram_count += seen[word]
            seen[word] += 1
        else:
            seen[word] = 1
        if anagram_count > 474:
            return False
    return True