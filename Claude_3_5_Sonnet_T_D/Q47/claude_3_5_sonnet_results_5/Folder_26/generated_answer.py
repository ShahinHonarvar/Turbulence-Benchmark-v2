def palindromes_of_specific_lengths(s):
    substring = s[24:85].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 21, min(i + 32, len(substring) + 1)):
            potential_palindrome = ''.join(filter(str.isalpha, substring[i:j]))
            if potential_palindrome == potential_palindrome[::-1] and 21 <= len(potential_palindrome) <= 31:
                palindromes.add(potential_palindrome)
    return palindromes