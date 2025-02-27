def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    english_only = ''.join(filter(str.isalpha, s[10:76]))
    palindromes = set()
    for start in range(len(english_only)):
        for length in range(10, 21):
            end = start + length
            if end <= len(english_only):
                substring = english_only[start:end]
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes