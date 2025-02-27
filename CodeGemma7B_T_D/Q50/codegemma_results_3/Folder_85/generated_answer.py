def if_contains_anagrams(str_list):
    str_count = {}
    for str in str_list:
        str = str.lower()
        str = ''.join(sorted(str))
        str_count[str] = str_count.get(str, 0) + 1
    anagram_count = 0
    for count in str_count.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 73