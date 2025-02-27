def if_contains_anagrams(strings):
    anagram_count = 0
    seen_anagrams = set()
    lower_strings = [s.lower() for s in strings if len(s) >= 3]
    for i in range(len(lower_strings)):
        for j in range(i + 1, len(lower_strings)):
            sorted_i = ''.join(sorted(lower_strings[i]))
            sorted_j = ''.join(sorted(lower_strings[j]))
            if sorted_i == sorted_j:
                anagram_pair = (sorted_i, sorted_j)
                if anagram_pair not in seen_anagrams:
                    anagram_count += 1
                    seen_anagrams.add(anagram_pair)
                if anagram_count > 98:
                    return False
    return True