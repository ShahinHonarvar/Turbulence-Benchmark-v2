def if_contains_anagrams(lst):
    count = 0
    used = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in used:
                continue
            used.add(sorted_word)
            for other_word in lst[lst.index(word) + 1:]:
                if len(other_word) >= 3 and ''.join(sorted(other_word.lower())) == sorted_word:
                    count += 1
    return count >= 69