def if_contains_anagrams(str_list):

    def is_anagram(str1, str2):
        if len(str1) != len(str2):
            return False
        str1 = sorted(str1.lower())
        str2 = sorted(str2.lower())
        return str1 == str2
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key].append(string)
        else:
            anagrams[key] = [string]
    if len(anagrams) <= 67:
        return True
    else:
        return False