def palindrome_of_length_at_least_n(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 6, len(s) + 1):
            sub_s = s[i:j]
            if all((char in 'abcdefghijklmnopqrstuvwxyz' for char in sub_s)) and is_palindrome(sub_s):
                palindromes.add(sub_s)
    return palindromes