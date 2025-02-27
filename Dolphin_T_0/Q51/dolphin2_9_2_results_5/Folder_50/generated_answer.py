def if_contains_anagrams(lst):
    count = 0
    anagrams_found = set()
    for word in lst:
        if len(word) >= 3:
            anagram = ''.join(sorted(word.lower()))
            if anagram in anagrams_found:
                count += 1
            else:
                anagrams_found.add(anagram)
    return count <= 47