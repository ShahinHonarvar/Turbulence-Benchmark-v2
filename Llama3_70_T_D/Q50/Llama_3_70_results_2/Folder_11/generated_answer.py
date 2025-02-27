def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagrams_count = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams_count:
            anagrams_count[sorted_word] += 1
        else:
            anagrams_count[sorted_word] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagrams_count.values()))
    return pairs_count >= 28