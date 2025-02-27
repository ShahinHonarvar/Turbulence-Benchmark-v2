def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    palindromes = set()
    substring = s[100:301]
    for length in range(50, 101):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub)
    return palindromes