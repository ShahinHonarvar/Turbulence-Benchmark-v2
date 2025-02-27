def if_contains_anagrams(lst):
    anagram_count = 0
    for word in lst:
        for other_word in lst:
            if word.lower() != other_word.lower() and sorted(word.lower()) == sorted(other_word.lower()) and (len(word) >= 3):
                anagram_count += 1
    return anagram_count >= 411