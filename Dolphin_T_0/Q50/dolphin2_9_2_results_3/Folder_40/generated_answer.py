def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key not in anagram_dict:
                anagram_dict[key] = 1
            else:
                anagram_dict[key] += 1
                anagram_count += 1
    return anagram_count >= 3