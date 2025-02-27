def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted((c.lower() for c in s if c.isalpha())))
    anagram_dict = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_chars(string)
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count > 85:
                return False
    return True