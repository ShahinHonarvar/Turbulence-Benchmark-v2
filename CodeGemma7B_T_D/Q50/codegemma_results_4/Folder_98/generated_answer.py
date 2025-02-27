def if_contains_anagrams(strings):
    anagrams = {}
    anagrams_count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower().replace(' ', '')))
        if sorted_string in anagrams:
            anagrams[sorted_string]['count'] += 1
            if anagrams[sorted_string]['count'] >= 7:
                anagrams_count += 1
        else:
            anagrams[sorted_string] = {'count': 1, 'string': string.lower().replace(' ', '')}
    return anagrams_count >= 7