def if_contains_anagrams(strings):
    anagram_dict = {}
    for word in strings:
        w = word.lower()
        if len(w) >= 3:
            key = ''.join(sorted(w))
            if key in anagram_dict:
                anagram_dict[key].append(w)
            else:
                anagram_dict[key] = [w]
    anagram_pairs = sum((len(val) * (len(val) - 1) // 2 for val in anagram_dict.values()))
    return anagram_pairs <= 19