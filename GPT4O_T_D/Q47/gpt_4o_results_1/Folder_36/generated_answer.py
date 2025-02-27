def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    letter_string = ''.join([c for c in s[124:284] if c.isalpha()])
    palindromes = set()
    for length in range(115, 135):
        for i in range(len(letter_string) - length + 1):
            substring = letter_string[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes