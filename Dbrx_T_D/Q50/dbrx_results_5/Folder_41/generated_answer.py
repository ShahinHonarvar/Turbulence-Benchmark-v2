import itertools

def if_contains_anagrams(strings_list):
    anagrams_count = 0
    for length in range(3, len(max(strings_list, key=len)) + 1):
        words_by_length = [word for word in strings_list if len(word) == length]
        anagrams = [set(p) for p in itertools.product(words_by_length, repeat=2) if ''.join(sorted(p[0])) == ''.join(sorted(p[1])) and p[0] != p[1]]
        anagrams_count += len(anagrams)
        if anagrams_count >= 75:
            return True
    return False