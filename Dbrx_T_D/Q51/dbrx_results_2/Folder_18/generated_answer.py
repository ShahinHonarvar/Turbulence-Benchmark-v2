import string

def if_contains_anagrams(string_list):
    anagram_count = 0
    english_letters = set(string.ascii_lowercase)
    for string1 in string_list:
        if len(string1) < 3:
            continue
        sorted_string1 = ''.join(sorted(filter(english_letters.__contains__, string1.lower())))
        for string2 in string_list:
            if string1 == string2:
                continue
            sorted_string2 = ''.join(sorted(filter(english_letters.__contains__, string2.lower())))
            if sorted_string1 == sorted_string2:
                anagram_count += 1
                if anagram_count > 42:
                    return False
                break
    return True