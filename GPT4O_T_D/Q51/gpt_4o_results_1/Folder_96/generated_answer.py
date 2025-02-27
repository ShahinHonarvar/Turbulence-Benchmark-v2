def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    seen = {}
    pairs = 0
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    for count in seen.values():
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 2:
                return False
    return True