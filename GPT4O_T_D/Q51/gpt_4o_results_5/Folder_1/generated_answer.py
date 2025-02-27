def if_contains_anagrams(lst):
    count = 0
    seen = {}
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in seen:
            count += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
        if count > 30:
            return False
    return True