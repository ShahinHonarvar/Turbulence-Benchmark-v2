def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[31:75]
    palindromes = set()
    for length in range(23, 40):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub.isalpha() and is_palindrome(sub):
                palindromes.add(sub)
    return palindromes