from collections import defaultdict

def palindromes_of_specific_lengths(s):
    s = s.lower()

    def is_palindrome(substring):
        return substring == substring[::-1]
    palindromes = set()
    for i in range(62, 89):
        for length in range(18, 22):
            if i + length <= 89:
                substring = s[i:i + length]
                if is_palindrome(substring) and all((c.isalpha() for c in substring)):
                    palindromes.add(substring)
    return palindromes