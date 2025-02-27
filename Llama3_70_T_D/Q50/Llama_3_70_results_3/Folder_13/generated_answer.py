def if_contains_anagrams(strings):
    anagram_count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(set(strings[i].casefold()) & set(strings[j].casefold())) >= 3:
                sorted_i = sorted(strings[i].casefold())
                sorted_j = sorted(strings[j].casefold())
                if sorted_i == sorted_j:
                    anagram_count += 1
    return anagram_count >= 144