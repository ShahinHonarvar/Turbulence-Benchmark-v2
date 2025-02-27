def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    anagram_count = 0
    for string in strings:
        if len(string) >= 3:
            normalized_string = normalize(string)
            if normalized_string in anagram_dict:
                anagram_count += anagram_dict[normalized_string]
                if anagram_count > 55:
                    return False
                anagram_dict[normalized_string] += 1
            else:
                anagram_dict[normalized_string] = 1
    return anagram_count <= 55