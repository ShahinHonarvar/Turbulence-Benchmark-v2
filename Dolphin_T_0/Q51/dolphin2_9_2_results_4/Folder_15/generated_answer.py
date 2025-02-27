def if_contains_anagrams(lst):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    count = sum((1 for word1 in lst for word2 in lst if word1.lower() != word2.lower() and sorted(word1.lower()) in sorted(letters) and (sorted(word2.lower()) in sorted(letters)) and (len(word1) >= 3) and (len(word2) >= 3) and (sorted(word1.lower()) == sorted(word2.lower()))))
    return count <= 20