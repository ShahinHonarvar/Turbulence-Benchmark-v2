import collections

def if_contains_anagrams(str_list):

    def is_anagram(word1, word2):
        word1 = sorted(collections.Counter(word1.lower()).items())
        word2 = sorted(collections.Counter(word2.lower()).items())
        return word1 == word2

    def find_anagrams(str_list):
        anagrams = []
        for i in range(len(str_list)):
            for j in range(i + 1, len(str_list)):
                if is_anagram(str_list[i], str_list[j]):
                    anagrams.append((str_list[i], str_list[j]))
        return anagrams
    anagrams = find_anagrams(str_list)
    return len(anagrams) <= 206