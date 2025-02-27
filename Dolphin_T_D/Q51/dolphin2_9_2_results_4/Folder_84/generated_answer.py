import collections

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return s1.lower() == s2.lower() and sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_anagram(words[i], words[j]) and len(words[i]) >= 3 and (len(words[j]) >= 3):
                count += 1
                if count > 16:
                    return False
    return count <= 16