def if_contains_anagrams(strings):

    def sorted_lower_string(s):
        return ''.join(sorted(s.lower()))
    n = len(strings)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3:
                if sorted_lower_string(strings[i]) == sorted_lower_string(strings[j]):
                    count += 1
                    if count >= 88:
                        return True
    return False