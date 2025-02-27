def if_contains_anagrams(lst):
    anagrams_count = {}
    for word in lst:
        cleaned_word = ''.join((e for e in word if e.isalpha())).lower()
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word in anagrams_count:
            anagrams_count[sorted_word] += 1
        else:
            anagrams_count[sorted_word] = 1
    pairs_count = sum((x * (x - 1) // 2 for x in anagrams_count.values()))
    return pairs_count <= 58