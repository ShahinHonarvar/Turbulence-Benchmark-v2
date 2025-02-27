def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    sub_s = s[1:9]
    letters = [c for c in sub_s if c.isalpha()]
    palindromes = {''.join(letters).lower()}
    while len(letters) > 2:
        letters.pop()
        if is_palindrome(''.join(letters).lower()):
            palindromes.add(''.join(letters).lower())
        letters = [c for c in sub_s if c.isalpha() and c not in letters]
    return palindromes