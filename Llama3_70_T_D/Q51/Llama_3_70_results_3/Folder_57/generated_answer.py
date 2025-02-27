def if_contains_anagrams(lst):
    anagram_count = 0
    lst = [''.join(filter(str.isalpha, s)).lower() for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                anagram_count += 1
                if anagram_count > 74:
                    return False
    return True