import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_between_indices = s[4:10]
    English_letters_between_indices = set([ch for ch in s_between_indices if ch in English_letters])
    if len(English_letters_between_indices) < 2:
        return set()
    I = range(len(English_letters_between_indices) + 1)
    palindromes = set()
    for n in I[4:]:
        for subset in itertools.combinations(English_letters_between_indices, n):
            if is_palindrome(''.join(list(subset))):
                palindromes.add(''.join(list(subset)))
    return palindromes