def if_contains_anagrams(string_list):
    anagram_count = 0
    string_list = [s.lower() for s in string_list if len(s) >= 3]
    for i in range(len(string_list)):
        for j in range(i + 1, len(string_list)):
            if sorted(string_list[i]) == sorted(string_list[j]):
                anagram_count += 1
                if anagram_count >= 50:
                    return True
    return False