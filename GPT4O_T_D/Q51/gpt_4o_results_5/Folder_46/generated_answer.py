def if_contains_anagrams(lst):
    anagram_count = 0
    normalized = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    n = len(normalized)
    for i in range(n):
        for j in range(i + 1, n):
            if normalized[i] == normalized[j]:
                anagram_count += 1
                if anagram_count > 61:
                    return False
    return True