import itertools

def if_contains_anagrams(string_list):
    anagram_count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            for i in range(2, len(sorted_string) + 1):
                for j in itertools.combinations(range(len(sorted_string)), i):
                    anagram_count += 1 if ''.join((sorted_string[k] for k in j)) in string_list else 0
                    if anagram_count > 48:
                        return False
    return True