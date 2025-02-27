def if_contains_anagrams(strings):

    def char_count(s):
        count = [0] * 26
        for char in s:
            if char.isalpha():
                count[ord(char.lower()) - ord('a')] += 1
        return tuple(count)
    anagram_count = 0
    strings = [s for s in strings if len(s) >= 3]
    seen = set()
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if char_count(strings[i]) == char_count(strings[j]):
                pair = frozenset([i, j])
                if pair not in seen:
                    seen.add(pair)
                    anagram_count += 1
                    if anagram_count > 16:
                        return False
    return True