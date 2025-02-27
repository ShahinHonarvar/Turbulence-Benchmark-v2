def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized_strings = [sorted_str(s) for s in strings if len(s) >= 3]
    n = len(normalized_strings)
    for i in range(n):
        for j in range(i + 1, n):
            if normalized_strings[i] == normalized_strings[j]:
                count += 1
                if count >= 75:
                    return True
    return False