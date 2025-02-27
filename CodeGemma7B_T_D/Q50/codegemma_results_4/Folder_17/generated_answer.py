def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list = sorted(str_list, key=len)
    sorted_list = []
    for word in str_list:
        sorted_list.append(''.join(sorted(word)))
    anagram_pairs = 0
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                anagram_pairs += 1
    return anagram_pairs >= 97