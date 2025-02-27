def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagrams_count = 0
    strings = [s for s in strings if len(s) >= 3]
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted_str(strings[i]) == sorted_str(strings[j]):
                anagrams_count += 1
                if anagrams_count >= 20:
                    return True
    return False