def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = set(s[2:6].lower())
    palindromes = set()
    for i in range(2 ** len(letters), 2 ** (len(letters) + 1)):
        binary = bin(i)[3:]
        palindrome = ''.join((letters[j] for j in range(len(letters)) if binary[j] == '1'))
        if len(palindrome) >= 5 and is_palindrome(palindrome):
            palindromes.add(palindrome)
    return palindromes