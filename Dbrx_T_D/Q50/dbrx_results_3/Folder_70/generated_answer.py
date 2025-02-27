def if_contains_anagrams(strings):

    def sort_string(s):
        return ''.join(sorted(s))
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = sort_string(string.lower())
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    total_anagrams = sum(anagrams.values())
    return total_anagrams >= 189