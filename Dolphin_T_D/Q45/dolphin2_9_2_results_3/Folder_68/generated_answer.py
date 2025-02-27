import string
    from itertools import combinations

def palindromes_between_indices(s):
    palindrome_set = set()

    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]
    english_letters = set(string.ascii_lowercase)
    string_between_indices = s[1:9]
    combinations_between_indices = [''.join(comb) for i in range(len(string_between_indices)) for comb in combinations(string_between_indices, i)]
    for word in combinations_between_indices:
        if all([c in english_letters for c in word]):
            word_palindrome = ''.join([c for c in word if is_palindrome(c)])
            if len(word_palindrome) >= 4:
                palindrome_set.add(word_palindrome)
    return palindrome_set