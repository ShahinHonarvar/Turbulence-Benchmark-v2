def if_contains_anagrams(strings):

    def is_anagram(s, t):
        return sorted(s.lower()) == sorted(t.lower())
    anagrams = [string for string in strings if len(string) >= 3]
    anagrams.sort(key=lambda x: tuple(sorted(x)))
    count = 0
    for i in range(len(anagrams) - 1):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] != anagrams[j] and is_anagram(anagrams[i], anagrams[j]):
                count += 1
                if count >= 89:
                    return True
    return False