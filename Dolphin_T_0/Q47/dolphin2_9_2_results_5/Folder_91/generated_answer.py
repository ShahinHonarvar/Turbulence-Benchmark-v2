def palindromes_of_specific_lengths(s):
    s = s[0:11]
    length_3_5 = range(3, 6)
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in length_3_5:
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                l_substring = substring.lower()
                if is_palindrome(l_substring):
                    palindromes.add(l_substring)
    return palindromes