def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        cleaned_word = ''.join((char for char in word.lower() if char.isalpha()))
        if len(cleaned_word) < 3:
            continue
        sorted_word = ''.join(sorted(cleaned_word))
        if sorted_word in anagram_dict:
            count += len(anagram_dict[sorted_word])
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    return count <= 318