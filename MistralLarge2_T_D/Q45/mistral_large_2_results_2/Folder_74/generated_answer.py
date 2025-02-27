def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:7] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    palindromes = set()
    for i in range(len(lower_letters)):
        for j in range(i + 5, len(lower_letters) + 1):
            substring = lower_letters[i:j]
            if is_palindrome(substring):
                palindromes.add(''.join(substring))
    return palindromes