def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def filter_letters(sub):
        return ''.join((char for char in sub if char.isalpha()))
    s = s[12:93].lower()
    palindromes = set()
    for length in range(17, 67):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            filtered = filter_letters(substring)
            if is_palindrome(filtered) and 17 <= len(filtered) <= 66:
                palindromes.add(filtered)
    return palindromes