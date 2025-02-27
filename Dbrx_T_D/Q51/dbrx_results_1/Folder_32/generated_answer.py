import itertools

def if_contains_anagrams(list_of_strings):
    anagrams = {}
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
                if anagrams[sorted_string] > 1 and len(list(filter(lambda x: x > 1, anagrams.values()))) > 88:
                    return True
            else:
                anagrams[sorted_string] = 1
    return False