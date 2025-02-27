def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_set = set()
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) >= 3 and lower_string.isalpha():
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagram_set:
                anagram_count += 1
            anagram_set.add(sorted_string)
            if anagram_count > 3:
                return False
    return True