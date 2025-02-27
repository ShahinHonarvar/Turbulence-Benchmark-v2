def palindromes_of_specific_lengths(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    palindrome_set = set()
    for i in range(10, 60):
        for length in range(18, 37):
            if i + length <= 60:
                substring = s[i:i + length]
                if substring.lower() == substring.lower()[::-1] and english_letters.issuperset(substring):
                    palindrome_set.add(substring)
    return palindrome_set