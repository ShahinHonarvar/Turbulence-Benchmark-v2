def if_contains_anagrams(str_list):
    str_list = [''.join(filter(str.isalpha, s)).lower() for s in str_list if len(s) >= 3]
    anagrams = {}
    count = 0
    for s in str_list:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += anagrams[sorted_s]
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    return count <= 48