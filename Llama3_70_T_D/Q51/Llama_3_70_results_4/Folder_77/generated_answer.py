def if_contains_anagrams(lst):
    count = 0
    sorted_strings = [''.join(sorted(s.casefold())) for s in lst if s.isalpha() and len(s) >= 3]
    for i in range(len(sorted_strings)):
        for j in range(i + 1, len(sorted_strings)):
            if sorted_strings[i] == sorted_strings[j]:
                count += 1
                if count > 17:
                    return False
    return True