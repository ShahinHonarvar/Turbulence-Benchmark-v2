def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_dict = {}
    count_pairs = 0
    for string in strings:
        key = sorted_chars(string)
        if len(key) >= 3:
            if key in anagram_dict:
                anagram_dict[key].append(string)
            else:
                anagram_dict[key] = [string]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count_pairs += 1
            if count_pairs > 3:
                return False
    return True