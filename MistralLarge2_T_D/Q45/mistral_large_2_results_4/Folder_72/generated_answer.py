def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[1:8].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            subseq = letters[i:i + length]
            if is_palindrome(''.join(subseq)):
                palindromes.add(''.join(subseq))
    return palindromes