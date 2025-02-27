def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    anagram_count = 0
    checked_pairs = set()
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                pair = tuple(sorted((strings[i], strings[j])))
                if pair not in checked_pairs:
                    checked_pairs.add(pair)
                    anagram_count += 1
                    if anagram_count >= 20:
                        return True
    return False