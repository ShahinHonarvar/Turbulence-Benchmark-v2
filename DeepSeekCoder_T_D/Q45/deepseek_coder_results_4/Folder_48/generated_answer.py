def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[6:9].lower()))
    palindromes = set()
    for i in range(2 ** len(letters)):
        combination = ''.join((letters[j] for j in range(len(letters)) if i & 1 << j))
        if len(combination) >= 4 and is_palindrome(combination):
            palindromes.add(combination)
    return palindromes