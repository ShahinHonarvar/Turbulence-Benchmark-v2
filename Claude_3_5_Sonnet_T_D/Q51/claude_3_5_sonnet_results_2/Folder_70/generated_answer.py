def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            str1 = ''.join(filter(str.isalpha, string_list[i]))
            str2 = ''.join(filter(str.isalpha, string_list[j]))
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_count += 1
                if anagram_count > 97:
                    return False
    return True