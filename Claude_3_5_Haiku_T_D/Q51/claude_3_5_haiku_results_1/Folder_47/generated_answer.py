def if_contains_anagrams(words):

    def is_valid_anagram(a, b):
        return len(a) >= 3 and len(b) >= 3 and (sorted(a.lower()) == sorted(b.lower()))
    anagram_count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_valid_anagram(words[i], words[j]):
                anagram_count += 1
                if anagram_count > 366:
                    return False
    return True