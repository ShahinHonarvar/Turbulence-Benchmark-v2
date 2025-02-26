def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]

    def is_letters_only(sub):
        return sub.isalpha()
    palindromes = set()
    if len(s) < 95:
        return palindromes
    substring = s[23:95]
    for length in range(17, 56):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and is_letters_only(sub):
                palindromes.add(sub.lower())
    return palindromes