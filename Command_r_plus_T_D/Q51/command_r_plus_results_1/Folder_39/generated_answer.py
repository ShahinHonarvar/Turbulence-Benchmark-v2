def if_contains_anagrams(str_list: list[str]) -> bool:
    anagram_count = 0
    str_set = set()
    for str_ in str_list:
        cleaned_str = ''.join(filter(str.isalpha, str_.lower()))
        if len(cleaned_str) < 3:
            continue
        sorted_str = ''.join(sorted(cleaned_str))
        if sorted_str in str_set:
            anagram_count += 1
        else:
            str_set.add(sorted_str)
    return anagram_count <= 257