def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x == x[::-1]
    substring = s[125:284].lower()
    palindromes = set()
    for i in range(len(substring)):
        for length in range(109, 127):
            if i + length <= len(substring):
                candidate = substring[i:i + length]
                if is_palindrome(candidate) and candidate.isalpha():
                    palindromes.add(candidate)
    return palindromes