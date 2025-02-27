import sortedcollection

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = tuple(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string not in anagrams:
                anagrams[sorted_string] = []
            anagrams[sorted_string].append(string)
    count = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            count += len(anagrams[key]) * (len(anagrams[key]) - 1) // 2
    return count >= 70