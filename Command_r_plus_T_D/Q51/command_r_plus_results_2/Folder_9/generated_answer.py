def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join((e for e in text.lower() if e.isalpha()))

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    str_set = set()
    for str1 in lst:
        normalized_str1 = normalize_text(str1)
        if len(normalized_str1) < 3:
            continue
        for str2 in lst:
            if str1 == str2:
                continue
            normalized_str2 = normalize_text(str2)
            if is_anagram(normalized_str1, normalized_str2):
                if (str1, str2) not in str_set and (str2, str1) not in str_set:
                    anagram_count += 1
                    str_set.add((str1, str2))
                    if anagram_count > 475:
                        return False
    return True