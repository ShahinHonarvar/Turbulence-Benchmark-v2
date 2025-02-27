def if_contains_anagrams(lst):
    a_count = 0
    a_pairs = [0 for _ in range(26)]
    for string in lst:
        if len(string) < 3:
            continue
        sorted_lower = ''.join(sorted(string.lower()))
        if a_pairs[ord(sorted_lower[0]) - ord('a')] == 0:
            a_pairs[ord(sorted_lower[0]) - ord('a')] = 1
        else:
            a_count += 1
    return a_count <= 26