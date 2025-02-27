import string

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s).intersection(string.ascii_lowercase)

    def is_palindrome(s):
        return s == s[::-1]
    return {s for i in range(3, len(letters) + 1) for s in product(letters, repeat=i) if is_palindrome(s)}