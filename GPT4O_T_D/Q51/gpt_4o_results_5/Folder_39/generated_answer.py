def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)

    def normalize(s):
        return ''.join(sorted((char for char in s.lower() if char.isalpha())))
    checked_pairs = set()
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            str1, str2 = (strings[i], strings[j])
            norm1, norm2 = (normalize(str1), normalize(str2))
            if len(norm1) >= 3 and is_anagram(norm1, norm2):
                pair = tuple(sorted((str1.lower(), str2.lower())))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    count += 1
                    if count > 257:
                        return False
    return True