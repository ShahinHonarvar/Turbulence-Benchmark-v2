def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        sorted_letters = ''.join(sorted(string.lower()))
        if sorted_letters not in anagrams:
            anagrams[sorted_letters] = []
        anagrams[sorted_letters].append(string)
    count = 0
    for key, values in anagrams.items():
        if len(values) >= 3:
            count += len(values) - 2
    return count >= 59