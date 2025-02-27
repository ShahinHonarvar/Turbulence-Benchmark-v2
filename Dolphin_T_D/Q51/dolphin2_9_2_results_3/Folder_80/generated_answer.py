def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        sorted_string = sorted(string.lower())
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            count = 0
            for other_string in strings:
                if sorted_string == sorted(other_string.lower()):
                    count += 1
            if count >= 2:
                anagrams[sorted_string] = anagrams.get(sorted_string, 0) + count
    return sum(anagrams.values()) // 2 <= 255