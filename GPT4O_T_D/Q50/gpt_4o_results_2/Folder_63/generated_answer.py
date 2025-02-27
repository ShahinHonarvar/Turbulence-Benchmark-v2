def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    count = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted_str(strings[i]) == sorted_str(strings[j])):
                count += 1
                if count >= 89:
                    return True
    return False