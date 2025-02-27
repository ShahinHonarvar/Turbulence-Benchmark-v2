def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    letters = [c for c in s[2:9] if c.isalpha()]
    length = len(letters)
    palindromes = set()
    for i in range(length):
        for j in range(i + 5, length + 1):
            sub = ''.join(letters[i:j]).lower()
            if is_palindrome(sub) and len(sub) >= 6:
                palindromes.add(sub)
    return palindromes