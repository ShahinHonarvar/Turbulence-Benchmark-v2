def palindromes_of_specific_lengths(s):

    def is_palindrome(s):
        return s == s[::-1]
    substring = s[0:5]
    lengths = [3, 4]
    palindromes = set()
    for length in lengths:
        for i in range(len(substring) - length + 1):
            sub = substring[i:length + i]
            if is_palindrome(sub) and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes