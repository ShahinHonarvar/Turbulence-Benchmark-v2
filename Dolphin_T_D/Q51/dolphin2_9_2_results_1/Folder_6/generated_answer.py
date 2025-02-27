def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word in seen:
                count += 1
            else:
                seen.add(sorted_word)
    return count <= 86