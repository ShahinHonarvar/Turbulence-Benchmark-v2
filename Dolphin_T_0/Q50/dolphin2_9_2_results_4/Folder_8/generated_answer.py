def if_contains_anagrams(lst):
    lowercase_lst = [s.lower() for s in lst]
    sorted_lowercase_lst = [''.join(sorted(s)) for s in lowercase_lst if len(s) >= 3]
    anagram_count = sum([i.count(j) // 2 for i in sorted_lowercase_lst for j in sorted_lowercase_lst if i == j and i != j])
    return anagram_count >= 85