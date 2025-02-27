import collections

def if_contains_anagrams(strings):
    anagrams = [[] for _ in range(26)]
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[ord(sorted_string[0]) - ord('a')].append(sorted_string)
    count = 0
    for group in anagrams:
        count += len(group) * (len(group) - 1) // 2
        if count >= 14:
            return True
    return False