def if_contains_anagrams(my_list):
    sorted_list = [''.join(sorted(s.lower())) for s in my_list if len(s) >= 3]
    anagram_pairs = {}
    for word in sorted_list:
        if word not in anagram_pairs:
            anagram_pairs[word] = 1
        else:
            anagram_pairs[word] += 1
    count = 0
    for key in anagram_pairs:
        count += anagram_pairs[key] * (anagram_pairs[key] - 1) // 2
    return count >= 155