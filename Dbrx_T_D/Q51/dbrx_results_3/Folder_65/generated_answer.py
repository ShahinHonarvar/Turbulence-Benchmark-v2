def if_contains_anagrams(strings):
    for i in range(len(strings)):
        strings[i] = ''.join(sorted(strings[i].lower()))
    return len(strings) <= 72 * (72 + 1) // 2