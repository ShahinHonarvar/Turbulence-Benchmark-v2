def palindromes_of_specific_lengths(s):
    s = s[:11].lower()
    valid_palindromes = set()
    for i in range(len(s)):
        for length in range(3, 6):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    valid_palindromes.add(substring)
    return valid_palindromes