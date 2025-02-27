import itertools

def is_anagram(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

def count_anagrams(words):
    anagrams = [word for word in words if len(word) >= 3]
    anagram_count = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if is_anagram(anagrams[i], anagrams[j]):
                anagram_count += 1
    return anagram_count

def if_contains_anagrams(word_list):
    return count_anagrams(word_list) <= 188