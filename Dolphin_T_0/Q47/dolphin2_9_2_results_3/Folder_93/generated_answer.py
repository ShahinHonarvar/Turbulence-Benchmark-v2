def palindromes_of_specific_lengths(s):
    substring = s[17:96]
    palindrome_set = set()
    for length in range(13, 50):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindrome_set.add(sub.lower())
    return palindrome_set