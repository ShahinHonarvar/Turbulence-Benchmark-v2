from itertools import permutations
    import string

def palindromes_between_indices(word):
    if word[2:8].lower().count('s') >= 2 and word[2:8].lower().count('t') >= 2 and (word[2:8].lower().count('e') >= 2):
        letters = list(string.ascii_lowercase)
        english_letters_in_word = set(word[2:8].lower())
        permutations_set = set()
        for i in permutations(letters, 5):
            if set(i).issubset(english_letters_in_word):
                permutations_set.add(''.join(i))
        return permutations_set
    return set()