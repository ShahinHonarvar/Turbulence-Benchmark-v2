from collections import defaultdict

def if_contains_anagrams(str_list):
    seen_anagrams = defaultdict(int)
    for string in str_list:
        processed_string = ''.join((c for c in string if c.isalpha())).lower()
        sorted_string = ''.join(sorted(processed_string))
        if sorted_string in seen_anagrams:
            seen_anagrams[sorted_string] += 1
            if seen_anagrams[sorted_string] > 464:
                return False
        else:
            seen_anagrams[sorted_string] = 1
    return True