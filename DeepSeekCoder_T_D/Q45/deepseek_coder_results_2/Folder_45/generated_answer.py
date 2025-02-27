def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[5:10].lower()))
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(combination) >= 4 and is_palindrome(combination):
            palindromes.add(combination)
    return palindromes