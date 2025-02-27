def palindromes_between_indices(s):

    def generate_palindromes(s):
        palindromes = set()
        for a in s:
            for b in s:
                for c in s:
                    palindrome = a + b + c
                    if palindrome == palindrome[::-1]:
                        palindromes.add(palindrome)
        return palindromes
    substring = ''.join([c for c in s[2:5] if c.isalpha()]).lower()
    return generate_palindromes(substring)