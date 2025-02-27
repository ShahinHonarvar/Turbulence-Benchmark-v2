import itertools

def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1].lower()
    index_5_to_8 = s[4:9]
    index_5_to_8 = ''.join([char for char in index_5_to_8 if char.isalpha()])
    pals = set()
    for length in range(5, len(index_5_to_8) + 1):
        for sub in itertools.combinations(index_5_to_8, length):
            pal = ''.join(sub)
            if is_palindrome(pal):
                pals.add(pal.lower())
    return pals