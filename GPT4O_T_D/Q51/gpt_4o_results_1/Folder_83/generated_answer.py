def if_contains_anagrams(strings):

    def sorted_letters(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    count = 0
    n = len(strings)
    anagram_set = set()
    for i in range(n):
        if len(strings[i]) < 3:
            continue
        sorted_s1 = sorted_letters(strings[i])
        for j in range(i + 1, n):
            if len(strings[j]) < 3:
                continue
            sorted_s2 = sorted_letters(strings[j])
            if sorted_s1 == sorted_s2:
                pair = tuple(sorted((strings[i].lower(), strings[j].lower())))
                if pair not in anagram_set:
                    anagram_set.add(pair)
                    count += 1
                    if count > 19:
                        return False
    return True