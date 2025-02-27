def palindromes_between_indices(str1):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(str1) - 5):
        for j in range(i + 7, len(str1)):
            substring = ''
            for letter in str1[i:j + 1].lower():
                if letter.isalpha():
                    substring += letter
            if is_palindrome(substring) and len(substring) >= 6:
                palindromes.add(substring)
    return palindromes