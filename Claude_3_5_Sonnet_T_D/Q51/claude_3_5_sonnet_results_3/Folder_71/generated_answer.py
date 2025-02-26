def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    processed = set()
    for i in range(len(string_list)):
        if i in processed:
            continue
        current = ''.join(filter(str.isalpha, string_list[i]))
        if len(current) < 3:
            continue
        for j in range(i + 1, len(string_list)):
            if j in processed:
                continue
            compare = ''.join(filter(str.isalpha, string_list[j]))
            if len(compare) < 3:
                continue
            if is_anagram(current, compare):
                anagram_count += 1
                processed.add(j)
                if anagram_count > 9:
                    return False
        processed.add(i)
    return True