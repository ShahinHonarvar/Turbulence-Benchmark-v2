def if_contains_anagrams(lst):
    anagrams_count = 0
    seen = set()
    for word in lst:
        word_lower = ''.join(sorted(word.lower()))
        if word_lower in seen:
            continue
        for other_word in lst[lst.index(word) + 1:]:
            other_word_lower = ''.join(sorted(other_word.lower()))
            if word_lower == other_word_lower and len(word) >= 3 and word_lower.isalpha():
                anagrams_count += 1
    return anagrams_count <= 9