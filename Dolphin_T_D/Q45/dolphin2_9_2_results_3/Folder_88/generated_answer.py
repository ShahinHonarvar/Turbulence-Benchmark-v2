def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = ''.join([char for char in s[3:8] if char.isalpha()])
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 5, len(letters) + 1):
            segment = letters[i:j]
            if is_palindrome(segment):
                palindromes.add(segment)
    return palindromes