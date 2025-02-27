def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[200:301].lower()
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and candidate.isalpha():
                palindromes.add(candidate)
    return palindromes