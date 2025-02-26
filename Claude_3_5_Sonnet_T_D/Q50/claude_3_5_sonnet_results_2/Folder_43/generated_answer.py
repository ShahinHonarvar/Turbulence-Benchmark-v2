def if_contains_anagrams(string_list):
    anagram_count = 0
    string_list = [s.lower() for s in string_list if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in string_list]
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if sorted_strings[i] == sorted_strings[j]:
                anagram_count += 1
                if anagram_count >= 61:
                    return True
    return False