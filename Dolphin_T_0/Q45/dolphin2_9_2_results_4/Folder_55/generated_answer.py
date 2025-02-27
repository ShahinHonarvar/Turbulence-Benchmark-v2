import itertools

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[:3].lower()
    letters = set(substring) - set('\\W')
    if len(letters) < 3:
        return set()
    arrangements = [''.join(i) for i in itertools.product(letters, repeat=len(substring))]
    palindromes = [arrangement for arrangement in arrangements if is_palindrome(arrangement) and len(arrangement) >= 3]
    return set(palindromes)