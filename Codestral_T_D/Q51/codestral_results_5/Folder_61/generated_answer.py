def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for word in strings:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
                anagram_count += 1
            else:
                anagram_dict[sorted_word] = [word]
    return anagram_count <= 50