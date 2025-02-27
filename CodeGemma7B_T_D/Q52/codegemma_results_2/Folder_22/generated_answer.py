def palindrome_of_length_n(s):

    def isPalindrome(word):
        return word == word[::-1]
    set_of_palindromes = set()
    for i in range(len(s) - 19):
        for j in range(i + 20, len(s) + 1):
            substring = s[i:j]
            if isPalindrome(substring.lower()) and substring.isalpha():
                set_of_palindromes.add(substring)
    return set_of_palindromes