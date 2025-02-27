import string

def if_contains_anagrams(strings):
    anagrams = {}
    max_pairs = 131
    num_pairs = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower())).strip(string.punctuation)
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
            if anagrams[sorted_s] == 2:
                num_pairs += 1
                if num_pairs > max_pairs:
                    return False
    return True