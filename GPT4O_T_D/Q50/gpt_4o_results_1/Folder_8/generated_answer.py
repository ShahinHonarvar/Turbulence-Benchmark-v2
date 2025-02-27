from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    words = [word.lower() for word in words]
    valid_words = [word for word in words if len(word) >= 3]
    anagrams_dict = defaultdict(list)
    for word in valid_words:
        sorted_word = ''.join(sorted(word))
        anagrams_dict[sorted_word].append(word)
    count = 0
    for group in anagrams_dict.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count >= 85