def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lowered = string.lower()
        sorted_str = ''.join(sorted(lowered))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(lowered)
        else:
            anagrams[sorted_str] = [lowered]
    for anagram_list in anagrams.values():
        if len(anagram_list) > 1 and len(anagram_list[0]) >= 3:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count >= 8