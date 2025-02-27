from itertools import permutations
    import string as st

def palindromes_between_indices(string):
    string = string[1:4].lower()
    english_letters = set(st.ascii_lowercase)
    all_perms = ''.join(english_letters)
    palindromes = set()
    for p in permutations(string, len(string)):
        for perm in all_perms:
            new_word = ''.join(p) + perm
            if new_word == new_word[::-1] and len(new_word) >= 4:
                palindromes.add(new_word)
    return palindromes if palindromes else set()