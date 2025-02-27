def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagrams:
                count += anagrams[sorted_str]
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    return count <= 401