def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[2:7])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(2 ** n):
        combination = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(combination) >= 5 and is_palindrome(combination):
            palindromes.add(combination)
    return palindromes