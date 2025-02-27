def palindromes_of_specific_lengths(s):
    english_lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for length in range(3, 11):
        for start in range(1, 300 - length + 1):
            palindrome = s[start:start + length]
            if palindrome.lower() == palindrome.lower()[::-1] and palindrome.isalpha() and (len(palindrome) == length):
                palindromes.add(palindrome)
    return palindromes