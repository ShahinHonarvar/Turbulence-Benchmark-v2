def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1].lower()
    letters = [char for char in s[5:8] if char.isalpha()]
    return {''.join(word) for word in itertools.permutations(letters, len(letters)) if is_palindrome(''.join(word)) and len(''.join(word)) >= 4}