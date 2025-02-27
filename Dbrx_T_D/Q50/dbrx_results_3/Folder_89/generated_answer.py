import string

def if_contains_anagrams(string_list):
    anagrams = {}
    for word in string_list:
        cleaned_word = ''.join((c.lower() for c in word if c not in string.punctuation))
        sorted_word = ''.join(sorted(cleaned_word))
        if len(sorted_word) >= 3:
            if sorted_word not in anagrams:
                anagrams[sorted_word] = [cleaned_word]
            else:
                anagrams[sorted_word].append(cleaned_word)
    anagram_pairs = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return anagram_pairs >= 36