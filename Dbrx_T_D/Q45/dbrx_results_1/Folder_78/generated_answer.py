def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

def palindromes_between_indices(s):
    chars = s[6:9]
    words = [''.join(char_set) for char_set in itertools.product('abcdefghijklmnopqrstuvwxyz', repeat=len(chars)) if set(chars) >= set(char_set)]
    palindromes = set((word for word in words if is_palindrome(word) and len(word) >= 3))
    return palindromes