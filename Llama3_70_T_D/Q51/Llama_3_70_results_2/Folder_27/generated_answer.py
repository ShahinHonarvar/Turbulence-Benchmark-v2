def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for num in anagrams.values():
        if num > 1:
            count += num * (num - 1) // 2
        if count > 113:
            return False
    return True