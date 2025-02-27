import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                count += 1
                if count >= 95:
                    return True
            else:
                anagrams[sorted_string] = 1
    return False