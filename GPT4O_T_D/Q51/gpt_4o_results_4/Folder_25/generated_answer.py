def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    normalized_strings = [''.join(filter(str.isalpha, s)).lower() for s in strings]
    count = 0
    for i in range(len(normalized_strings)):
        if len(normalized_strings[i]) < 3:
            continue
        for j in range(i + 1, len(normalized_strings)):
            if len(normalized_strings[j]) < 3:
                continue
            if is_anagram(normalized_strings[i], normalized_strings[j]):
                count += 1
                if count > 67:
                    return False
    return True